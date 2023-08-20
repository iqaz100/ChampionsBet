from enum import Enum


class INVITATION_STATUSES_ENUM(Enum):
    pending = 'PENDING'
    accepted = 'ACCEPTED'
    declined = 'DECLINED'


INVITATION_STATUSES = [
    INVITATION_STATUSES_ENUM.pending.value,
    INVITATION_STATUSES_ENUM.accepted.value,
    INVITATION_STATUSES_ENUM.declined.value,
]
