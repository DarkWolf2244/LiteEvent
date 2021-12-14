from . import Events

events = Events(allow_nonexistent_events=False)

events.add_events(['camera.picture.before'])
@events.on('camera.picture.before')
def camera_picture_before(announcement):
    print(f"We're about to take a picture! {announcement}")

events.emit('camera.picture.before', "Say cheese!")