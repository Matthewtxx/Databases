"""forms.py"""

from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import SelectField

class PlaylistForm(FlaskForm):
    """Form for adding a playlist."""

    name = StringField("Playlist Name", validators=[DataRequired()])
    description = TextAreaField("Description")  # Add the 'description' field
    submit = SubmitField("Add Playlist")


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Title', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    submit = SubmitField('Create Song')


class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""
    song = SelectField('Song To Add', coerce=int)
