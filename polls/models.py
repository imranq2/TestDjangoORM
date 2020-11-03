from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)


class Question(models.Model):
    name = models.CharField(max_length=20)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"name={self.name}, question_text={self.question_text}, pub_date={self.pub_date}" + \
            ",".join([str(c) for c in self.choice_set.all()])


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"choice_text={self.choice_text}, votes={self.votes}"
