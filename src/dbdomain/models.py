from tortoise import models, fields


class Command(models.Model):
    id = fields.UUIDField(pk=True)
    os = fields.CharField(max_length=5)
    description = fields.TextField(null=True)
    args = fields.TextField()

    class Meta:
        table = "commands"
    pass
