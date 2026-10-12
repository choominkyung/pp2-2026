# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 앨범(Album), 노래(Song), 가수(Artist), 재생목록(Playlist) 간의 has-a 관계를 구현한다.
# 설계:
# - Artist 클래스는 가수의 이름을 저장한다.
# - Album 클래스는 앨범 제목, 가수, 발표 연도 및 수록곡(tracks) 리스트를 관리한다.
# - Playlist 클래스는 재생목록 이름과 노래 목록을 관리하며 노래를 추가하는 기능을 가진다.

class Artist:
    def __init__(self, name):
        self.name = name  # 가수 이름

class Song:
    def __init__(self, title):
        self.title = title  # 노래 제목

class Album:
    def __init__(self, title, artist, year):
        self.title = title    # 앨범 제목
        self.artist = artist  # 가수 객체
        self.year = year      # 발표 연도
        self.tracks = []      # 수록곡 리스트

    # 앨범에 노래를 추가하는 메서드
    def add_track(self, song_title):
        song = Song(song_title)
        self.tracks.append(song)

class Playlist:
    def __init__(self, name):
        self.name = name    # 재생목록 이름
        self.songs = []     # 재생목록에 담긴 노래 리스트

    # 재생목록에 노래를 추가하는 메서드
    def add_song(self, song):
        self.songs.append(song)

# --- 객체 생성 및 실행 테스트 ---
lee = Artist("Lee's Band")
album = Album("첫 번째 앨범", lee, 2020)

album.add_track("첫 번째 노래")
album.add_track("두 번째 노래")

playlist = Playlist("애창곡")

# 앨범의 모든 수록곡을 재생목록에 추가
for song in album.tracks:
    playlist.add_song(song)

print(f"'{playlist.name}' 재생목록에 {len(playlist.songs)}곡이 추가되었습니다.")
