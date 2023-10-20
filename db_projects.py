from models.Products import Products
from models.models import InitEngine
from sqlmodel import select, desc
from models.Albums import Albums
from models.Tracks import Tracks


class SelectProjects(InitEngine):
    def __init__(self):
        super().__init__()
        self.all_singles = \
            self.session.execute(select(Tracks).join(Tracks.single).join(Tracks.artists).join(Tracks.text).group_by(Tracks))
        self.all_albums = \
            self.session.execute(select(Albums).join(Albums.tracks).join(Albums.artists).group_by(Albums))
        self.all_featurings = \
            self.session.execute(select(Tracks).join(Tracks.featuring).join(Tracks.artists).group_by(Tracks))
        self.all_products = self.session.execute(select(Products).order_by(Products.id))

    def select_one_album(self, album_id: int):
        db_albums_scalars = \
            self.session.execute(select(Albums).join(Albums.tracks).join(Albums.artists)
                                 .where(Albums.id == album_id)).scalars()
        result = None
        for album in db_albums_scalars:
            result = {
                'id': album.id, 'title': album.title, 'date_release': album.date_release.strftime('%d %B %Y'),
                'cover': album.cover, 'artists': album.artists, 'tracks': [
                    {
                        'position': track.track_position_in_album, 'title': track.title,
                        'duration': f'{str(track.duration).split(":")[0]}:{str(track.duration).split(":")[1]}',
                        'artists': track.artists, 'text': track.text
                    } for track in album.tracks
                ]
            }
        return result

    def select_all_albums(self):
        db_albums_scalars = self.all_albums.scalars()
        result = [
            {
                'id': album.id, 'title': album.title, 'date_release': album.date_release.strftime('%d %B %Y'),
                'cover': album.cover, 'artists': album.artists, 'tracks': [
                    {
                        'position': track.track_position_in_album, 'title': track.title,
                        'duration': f'{str(track.duration).split(":")[0]}:{str(track.duration).split(":")[1]}',
                        'artists': track.artists
                    } for track in album.tracks
                ]
            } for album in db_albums_scalars
        ]
        return result

    def select_singles(self):
        return self.all_singles.scalars()

    def select_featurings(self):
        return self.all_featurings.scalars()

    def select_last_releases(self):
        last_releases = []
        db_last_albums_scalars = self.session\
            .execute(select(Albums).join(Albums.artists).order_by(desc(Albums.date_release)).limit(3)).scalars()
        db_last_singles_scalars = self.session\
            .execute(select(Tracks).join(Tracks.single).join(Tracks.artists).group_by(Tracks)
                     .order_by(desc(Tracks.date_release)).limit(3)).scalars()
        for release in db_last_singles_scalars:
            last_releases.append({
                'id': release.id, 'title': release.title,
                'artists': release.artists, 'date_release': release.date_release
            })
        for release in db_last_albums_scalars:
            last_releases.append({
                'id': release.id, 'title': release.title, 'artists': release.artists,
                'date_release': release.date_release, 'is_album': True
            })
        last_releases.sort(key=lambda item: item['date_release'], reverse=True)
        return last_releases[:3]

    def select_products(self):
        db_products_scalars = self.all_products.scalars()
        return [
            {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'old_price': product.old_price
            } for product in db_products_scalars
        ]

