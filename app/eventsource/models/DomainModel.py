from datetime import datetime
from typing import Any, Dict
from uuid import UUID

from pydantic import BaseModel

from eventsourcing.domain import (
    Aggregate as BaseAggregate,
    CanInitAggregate,
    CanMutateAggregate,
    CanSnapshotAggregate
)


class DomainEvent(BaseModel):
    originator_id: UUID
    originator_version: int
    timestamp: datetime

    class Config:
        allow_mutation: False


class Aggregate(BaseAggregate):
    class Event(DomainEvent, CanMutateAggregate):
        pass

    class Created(Event, CanInitAggregate):
        originator_topic: str


class Snapshot(DomainEvent, CanSnapshotAggregate):
    topic: str
    state: Dict[str, Any]
