import graphene

from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from timetable.schemas.query.timetable import TimetableNode


class Query(graphene.ObjectType):
    training = relay.Node.Field(TimetableNode)
    trainings = DjangoFilterConnectionField(TimetableNode)


schema = graphene.Schema(query=Query)
