from bottle import route
from bottle import run
from bottle import request
from bottle import HTTPError
import album


@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    albums_num = album.number(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
#result = "Общее количество альбомов {}".format(album.album_cnt)
        result = "Количество найденных альбомов {}. Список альбомов {}<br>".format(albums_num, artist)
        result += "<br>".join(album_names)
    return result


@route("/albums", method="POST")
def user():
	user_data = request.forms.get("artist")
	user_data1 = request.forms.get("genre")
	user_data2 = request.forms.get("year")
	user_data3 = request.forms.get("album")
	try:
		int(user_data2)
	except ValueError:
		message = "неправильно введен год"
		result = HTTPError(500, message)
	else:
		album.save(user_data, user_data1, user_data2, user_data3)
		if album.save(user_data, user_data1, user_data2, user_data3) != 0:
			message = "Альбом уже существует"
			result = HTTPError(404, message)
		else:
			result = "Данные сохранены"
	return result

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
  
#http -f POST http://localhost:8080/albums artist="New"