from django.forms import ModelForm

from products.models import Comment, ShoppingCard, ReplayComment, BlogComments


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'message', 'product')


class CardForm(ModelForm):
    class Meta:
        model = ShoppingCard
        fields = ('quantity', 'product', 'user')


class ReplayCommentForm(ModelForm):
    class Meta:
        model = ReplayComment
        fields = ('message', 'rate', 'comment')


class BlogCommentForm(ModelForm):
    class Meta:
        model = BlogComments
        fields = ('fullname', 'email', 'comment')
