"""empty message

Revision ID: 6bc3bf2847b8
Revises: e64d34e2d126
Create Date: 2023-10-18 19:24:00.346001

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6bc3bf2847b8'
down_revision: Union[str, None] = 'e64d34e2d126'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('albumsartists')
    op.drop_table('featuringsartists')
    op.drop_table('albums')
    op.drop_table('artists')
    op.drop_table('artiststracks')
    op.drop_table('featurings')
    op.drop_table('albumstracks')
    op.drop_table('singles')
    op.drop_table('tracks')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tracks',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('tracks_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('duration', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('date_release', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('track_position_in_album', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tracks_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('singles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('track_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], name='singles_track_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='singles_pkey')
    )
    op.create_table('albumstracks',
    sa.Column('album_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('track_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], name='albumstracks_album_id_fkey'),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], name='albumstracks_track_id_fkey'),
    sa.PrimaryKeyConstraint('album_id', 'track_id', name='albumstracks_pkey')
    )
    op.create_table('featurings',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('featurings_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('track_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], name='featurings_track_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='featurings_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('artiststracks',
    sa.Column('track_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], name='artiststracks_artist_id_fkey'),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], name='artiststracks_track_id_fkey'),
    sa.PrimaryKeyConstraint('track_id', 'artist_id', name='artiststracks_pkey')
    )
    op.create_table('artists',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('artists_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='artists_pkey'),
    sa.UniqueConstraint('name', name='artists_name_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('albums',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('albums_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('date_release', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('cover', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='albums_pkey'),
    sa.UniqueConstraint('cover', name='albums_cover_key'),
    sa.UniqueConstraint('title', name='albums_title_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('featuringsartists',
    sa.Column('featuring_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], name='featuringsartists_artist_id_fkey'),
    sa.ForeignKeyConstraint(['featuring_id'], ['featurings.id'], name='featuringsartists_featuring_id_fkey'),
    sa.PrimaryKeyConstraint('featuring_id', 'artist_id', name='featuringsartists_pkey')
    )
    op.create_table('albumsartists',
    sa.Column('album_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], name='albumsartists_album_id_fkey'),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], name='albumsartists_artist_id_fkey'),
    sa.PrimaryKeyConstraint('album_id', 'artist_id', name='albumsartists_pkey')
    )
    # ### end Alembic commands ###
