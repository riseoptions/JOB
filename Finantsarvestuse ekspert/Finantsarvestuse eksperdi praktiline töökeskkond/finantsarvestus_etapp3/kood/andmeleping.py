"""Lisanduv tüübitud piir. Menetlusreeglid ja toorsisend säilivad."""
import re
from datetime import date
from decimal import Decimal
from typing import Annotated, Literal
from pydantic import BaseModel, ConfigDict, Field, BeforeValidator, ValidationError


def parse_cents(value):
    if type(value) is int:
        return value
    if isinstance(value, str) and re.fullmatch(r"[0-9]+", value):
        return int(value)
    raise ValueError('Raha peab olema täisarv sentides või numbritest CSV-tekst')


def parse_date(value):
    if type(value) is date:
        return value
    if isinstance(value, str) and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        return date.fromisoformat(value)
    raise ValueError('Vajalik ISO kuupäev')


def parse_rate(value):
    if isinstance(value, bool) or not isinstance(value, (str, Decimal, int, float)):
        raise ValueError('Vajalik arvuline käibemaksumäär')
    try:
        result=Decimal(str(value))
        if not result.is_finite(): raise ValueError('Määr peab olema lõplik arv')
        return result
    except ArithmeticError as e:
        raise ValueError('Vigane käibemaksumäär') from e

Cents=Annotated[int, Field(strict=True,ge=0,le=10**12), BeforeValidator(parse_cents)]
ISODate=Annotated[date, BeforeValidator(parse_date)]
Text=Annotated[str, Field(strict=True,min_length=1)]

class InvoiceInput(BaseModel):
    # status, note ja tulevased lisaveerud säilivad. Toor-JSON-i ei kirjutata ümber.
    model_config=ConfigDict(extra='allow',frozen=True)
    invoice_id: Text
    supplier_id: Text
    supplier_name: Text
    invoice_number: Text
    invoice_date: ISODate
    service_date: ISODate
    due_date: ISODate
    description: Text
    net_cents: Cents
    vat_cents: Cents
    gross_cents: Cents
    vat_rate: Annotated[Decimal, BeforeValidator(parse_rate)]
    cost_center: Text
    account: Text
    provenance: Literal['SUNTEETILINE']
    currency: Literal['EUR']='EUR'


def shape_issues(row):
    try:
        InvoiceInput.model_validate(row)
        return []
    except ValidationError as exc:
        return [dict(code='ANDMEKUJU',field='.'.join(map(str,e['loc'])),
                     message=e['msg'],severity='VIGA') for e in exc.errors()]
