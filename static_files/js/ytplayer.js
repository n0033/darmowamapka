
var player;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('youtube_clip', {
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {
    event.target.playVideo();
}

var done = false;

function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.ENDED) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", 'https://darmowamapka.pl/video_watched/', true);
        xhr.send("watched=True");
        window.location.replace("https://darmowamapka.pl/ebook_sent/")
    }
}

function stopVideo() {
    player.stopVideo();
}
