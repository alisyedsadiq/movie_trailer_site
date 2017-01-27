#import media.py for media class and fresh_tomatoes.py for making webpage from data
import media
import fresh_tomatoes
#movie variables
#1
dangal = media.Movie("Dangal", "A movie based on a wrestler father who makes his daughthers also wrestlers",
                     "http://images.mid-day.com/images/2015/sep/21-Dangal-first-look-Aamir.jpg#NOQA",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g#NOQA")
#2
raees = media.Movie("Raees", "A movie based on Underworld Don based on Gujrat",
                    "http://bollywoodlover.com/wp-content/uploads/2015/10/raees-poster.jpg","https://www.youtube.com/watch?v=J7_1MU3gDk0#NOQA")
#3
kaabil = media.Movie("Kaabil","A movie of a blind girl and boy",
                     "https://4.bp.blogspot.com/-qMtDBMuB-_g/WBDkMKDqN9I/AAAAAAAAKrQ/8rHxNM4MnSEDRpFPaYICkUZp_IjnDihpACLcB/s1600/Kaabil%2BMovie%2BPoster.jpg#NOQA",
                     "https://www.youtube.com/watch?v=nubDFeiUAsI$NOQA")
#4
kung_fu_yoga=media.Movie("Kung Fu Yoga",
                         "An India china joint venture movie based kung fu and yoga",
                         "http://img.goldposter.com/2016/09/kung-fu-yoga_poster_goldposter_com_3.jpg#NOQA",
                         "https://www.youtube.com/watch?v=hBgDWchCs0Y#NOQA")
#making a list
movies=[raees,kaabil,dangal,kung_fu_yoga]
#calling a function to make a webpage
fresh_tomatoes.open_movies_page(movies)
