import pytube as pt3

video = pt3.YouTube("https://www.youtube.com/watch?v=owglNL1KQf0")

video.streams.get_by_itag(248).download("YTVideos")