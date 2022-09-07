from .contentWords import wordsuco, wordsund, wordsuca, wordsem, wordsHome

# Common stuff
#######

techdict = {
        'python':{'icon':'static/icons/python.svg', 'name':'Python', 'link':'https://www.python.org'},
        'javascript':{'icon':'static/icons/javascript.svg', 'name':'JavaScript (JS)', 'link':'https://developer.mozilla.org/en-US/docs/Web/JavaScript'},
        'postgresql':{'icon':'static/icons/postgresql.svg','name':'PostgreSQL', 'link':'https://www.postgresql.org'},
        'html':{'icon':'static/icons/html.svg','name':'HTML', 'link':'https://developer.mozilla.org/en-US/docs/Web/HTML'},
        'css':{'icon':'static/icons/css.svg', 'name':'CSS', 'link':'https://developer.mozilla.org/en-US/docs/Web/CSS'},
        'flask':{'icon':'static/icons/flask.svg', 'name':'Flask', 'link':'https://flask.palletsprojects.com/en/2.2.x/'},
        'django':{'icon':'static/icons/django.svg', 'name':'Django', 'link':'https://www.djangoproject.com'},
        'github':{'icon':'static/icons/github.png', 'name':'GitHub', 'link':'https://github.com'},
        'heroku':{'icon':'static/icons/heroku.png', 'name':'Heroku', 'link':'https://www.heroku.com/'},
        'wordpress':{'icon':'static/icons/wordpress.svg', 'name':'WordPress', 'link':'https://wordpress.com'},
        'mongodb':{'icon':'static/icons/mongodb.svg', 'name':'MongoDB', 'link':'https://www.mongodb.com'},
        'bulma':{'icon':'static/icons/bulma.png', 'name':'Bulma', 'link':'https://bulma.io'},
        'bootstrap':{'icon':'static/icons/bootstrap.png', 'name':'Bootstrap', 'link':'https://getbootstrap.com'},
        'mysql':{'icon':'static/icons/mysql.svg', 'name':'MySQL', 'link':'https://www.mysql.com'},
    }

footer = {
    'techlist':['python','flask', 'bulma'],
    'techdict': techdict,
    'deployed':'heroku',
}


# pages
#######

home = {
    'title': 'Welcome',
    'quote': {
        'welcome': """"The fight is won or lost far away from witnesses - behind the lines, in the gym, and out there on the road, long before I dance under those lights." - Muhammad Ali""",
        'skills': """“What looks like talent is often careful preparation. What looks like skill is often persistent revision.” - James Clear""",
        'learn':""""You can't connect the dots looking forward; you can only connect them looking backward..." - Steve Jobs"""
    },
    'words': wordsHome,
    'icons': {
        'python':{'icon':'static/icons/python.svg', 'name':'Python', 'link':'https://www.python.org'},
        'javascript':{'icon':'static/icons/javascript.svg', 'name':'JavaScript (JS)', 'link':'https://developer.mozilla.org/en-US/docs/Web/JavaScript'},
        'mysql':{'icon':'static/icons/mysql.svg','name':'MySQL', 'link':'https://www.mysql.com'},
        'html':{'icon':'static/icons/html.svg','name':'HTML', 'link':'https://developer.mozilla.org/en-US/docs/Web/HTML'},
        'css':{'icon':'static/icons/css.svg', 'name':'CSS', 'link':'https://developer.mozilla.org/en-US/docs/Web/CSS'},
        'flask':{'icon':'static/icons/flask.svg', 'name':'Flask', 'link':'https://flask.palletsprojects.com/en/2.2.x/'},
        'django':{'icon':'static/icons/django.svg', 'name':'Django', 'link':'https://www.djangoproject.com'},
        'github':{'icon':'static/icons/github.png', 'name':'GitHub', 'link':'https://github.com'},
        'heroku':{'icon':'static/icons/heroku.png', 'name':'Heroku', 'link':'https://www.heroku.com/'},
        # 'wordpress':{'icon':'static/icons/wordpress.svg', 'name':'WordPress', 'link':'https://wordpress.com'},
        'mongodb':{'icon':'static/icons/mongodb.svg', 'name':'MongoDB', 'link':'https://www.mongodb.com'},
        'bulma':{'icon':'static/icons/bulma.png', 'name':'Bulma', 'link':'https://bulma.io'},
        'bootstrap':{'icon':'static/icons/bootstrap.png', 'name':'Bootstrap', 'link':'https://getbootstrap.com'},
    },
    'university':{
        'uco':{'images':'static/uco.png', 'title':'University of Colorado', 'words': wordsuco, 'link':'https://colorado.edu'},
        'und':{'images':'static/und.png', 'title':'University of Notre Dame', 'words': wordsund, 'link':'https://www.nd.edu'},
        'em':{'images':'static/em.png', 'title':'ExxonMobil', 'words': wordsem, 'link':'https://www.exxonmobil.com'},
        'uca':{'images':'static/uca.png', 'title':'University of California, Berkeley Extension', 'words': wordsuca, 'link':'https://extension.berkeley.edu'},
        
    },
    'footer': footer
}


projects = {
    'title':'Projects',
    'quote':"""
    Stay primitive. Trust the soup. Swing for the seats. Be ready for resistance. - Steven Pressfield
    """,
    'projects':{
        'stockmarket':{
            'title':'The Stock Market',
            'images':'static/stockmarket.png',
            'words':['This is a website I built to track and contextualize broad stock market.','The primary data set plotted in this site is the S&P 500 index.', 'This site makes use of some data analytic packages available in Python, specifically pandas, numpy and matplotlib'],
            'techlist':['python','flask','bootstrap', 'postgresql','heroku'],
            'techdict': techdict,
            'link':'https://lit-eyrie-84189.herokuapp.com',
            'github':'https://github.com/hansonjw/otium-python'
        },
        'nfl':{
            'title':'NFL Playoff Pickem league',
            'images':'static/nfl.svg',
            'words':['This webapp was built for my family NFL 2021 postseason pickem league.', 'Feel free to create an account, log in and see the functionality of the site.', 'This was my first Python/Flask app.  It utilizes a PostgreSQL database to store user information and the team selections.'],
            'techlist':['python','flask','bootstrap', 'postgresql', 'heroku'],
            'techdict': techdict,
            'link':'https://peaceful-everglades-01949.herokuapp.com/auth/login',
            'github':'https://github.com/hansonjw/hansonnfl_3'
        },
        'zookeeper':{
            'title':'Zoo KeepR',
            'images':'static/zookeepr.png',
            'words':['This webapp was built during the UC Berkeley web development course.', 'In this project I gained exposure to forms and handling POST requests.', 'I also gained some preliminary experience utilizing a MySQL database on the back end to store form data.'],
            'techlist':['javascript', 'html','css','mysql','heroku'],
            'techdict': techdict,
            'link':'https://pacific-island-81874.herokuapp.com/animals',
            'github':'https://github.com/hansonjw/zookeepr'
        },
        'techblog':{
            'title':'My First Blog',
            'images':'static/techblog.png',
            'words':['This webapp was built during the UC Berkeley web development course.','This is where I really started to understand requests, database interfaces, routes, and storing data.'],
            'techlist':['javascript', 'html','css','mysql', 'heroku',],
            'techdict': techdict,
            'link':'https://vast-fjord-84705.herokuapp.com',
            'github':'https://github.com/hansonjw/tech-blog'
        },
    },
    'footer':footer
}


contact = {
    'quote': "Please reach out through the links below if you would like to get in touch with me...",
    'contacts': ['linkedin', 'email', 'github', 'twitter'],
    'images': {
        'linkedin':'static/icons/linkedin.png',
        'email':'static/icons/email.png',
        'twitter':'static/icons/twitter.png',
        'github':'static/icons/github.png',
    },
    'links': {
        'linkedin':'https://www.linkedin.com/in/justinhanson1/',
        'email':'hansonjw@gmail.com',
        'twitter':'https://twitter.com/hansonjw',
        'github':'https://github.com/hansonjw',
    },
    'href': {
        'linkedin':'https://www.linkedin.com/in/justinhanson1/',
        'email':'mailto:hansonjw@gmail.com',
        'twitter':'https://twitter.com/hansonjw',
        'github':'https://github.com/hansonjw',
    },
    'footer':footer,
}

fun = {
    'title':'Interests',
    'quote' : """"Curiosity has its own reason for existing." - Albert Einstein""",
    'locs' : ['maroonbells', 'stream', 'mechazilla','garden', 'starbase','saturn5', 'midland', 'brk', 'pebble', 'carmel', 'cash', 'cashmace'],
    'images' : {
        'garden':'static/garden.jpeg',
        'maroonbells':'static/maroonbells.jpeg',
        'starbase':'static/starbase.jpeg',
        'mechazilla':'static/mechazilla.jpeg',
        'carmel':'static/carmel.jpeg',
        'stream':'static/stream.jpeg',
        'midland':'static/midland.jpeg',
        'brk':'static/brk.jpeg',
        'pebble':'static/pebble.jpeg',
        'saturn5':'static/saturn5.jpeg',
        'cash':'static/cash.jpeg',
        'cashmace':'static/cashmace.jpeg',
    },
    'words' : {
        'garden':["This is the SpaceX 'Rocket Garden' at Starbase where the older rockets are on display for the public.", "Wandering through the SpaceX facility and seeing all the progress they have made was such a fascinating experience.", "There is a lauch complex, as well as a humongous rocket manufacturing building.  It is incredible how close you can get."],
        'maroonbells':["This picture taken earlier this summer and is the famous 'Marroon Bells' just outside of Aspen, CO.", "Having grown up in Colorado I'll always love and appreciate the beauty of the mountains especially in the summertime."],
        'starbase':["Starbase Texas is a technology development facility for SpaceX located on the far Southern Tip of Texas.  Here they are developing the rockets and technology to take humanity to the Moon and Mars.", "The 'Starbase' sign is becoming a popular tourist stop and photo opportunity in Texas. The top of this long sign is tiled in solar panels."],
        'mechazilla':["This is a view from Boca Chica Beach looking back at the SpaceX launch complex.", "The launch and catch structure has been nicknamed 'Mechazilla' and is quite a sight to see.", "In the picture you can also see a heavy booster and a 'Starship' on the ground by the cranes."],
        'carmel':["The Monterey Penninsula is such a beautiful place.", "In this picture you can see a part of the famous Pebble Beach golf course."],
        'stream':["In Pfieffer Big Sur State Park we were surrounded by giant redwoods and sequoias (although there aren't any in this photo).", "The trees are indescribable, not to mention hard to capture in a photograph...",],
        'midland':["In 2015 at ExxonMobil I was assigned to the West Texas business unit.", "During this time, the United States became the largest oil producer in the world overtaking Saudia Arabia and Russia.  This U.S. oil production renaissance was driven by development of new fields in West Texas where ExxonMobil is a major player.", "This view of the oil fields is what you see as you fly into Midland.  Each 'pad' is an oil well and the extent to which oil fields cover the landscape left a strong impression on me to this day."],
        'brk':["Studying the writings of Warren Buffett has been one of the most import steps in my development as a business professional.", "Financial literacy and understanding investments has become a passion of mine, and in 2016 I attended the Berkshire Hathaway Annual meeting where I heard Mr. Buffett speak in person.", "Understanding how a kid from Omaha, Nebraska became one of the world's richest and most saavvy businessmen has been such an fortifying area of study for me."],
        'pebble':["Another stunning view of the California coast...the loan cypress.","There is something special about the Pacific Ocean.",],
        'saturn5':["If you are in Texas and you are interested in the space then the Johnson Space Center near Houston is a must see.", "On display here is a Saturn V rocket cobbled together with remaining parts from the Apollo program and missions. This massive rocket is what is required to propel three men to the moon!"],
        'cash':['Life can take you down some unexpected avenues.','This is Cash and we found him in the bushes of the house accross the street.  We took him in, nursed him back to health, and started working with a local animal rescue to find him a permanent home.',"Cash was adopted in July and has found a loving home!  Helping Cash find his way in the world was such an unexpected and fulfilling experience."],
        'cashmace':['We live in a cat friendly neighborhood and on the same day we met Cash, Mace (larger eared kitten on the right) came to our doorstep. Mace was really affraid of humans, and quite wild in a primal sense.','We ended up fostering him as well.  It has been such a joy to see him transform into the friendly and fun loving kitten he has become.','We are currently looking for the right home for him.'],
    },
    'links' : {
        'garden':'https://goo.gl/maps/ao5J71RrhYNk6t8r7',
        'maroonbells':"https://goo.gl/maps/KV2tuxrd3RKb1wRv6",
        'starbase':'https://goo.gl/maps/ao5J71RrhYNk6t8r7',
        'mechazilla': "https://goo.gl/maps/kdun97NejvLk1uvg6",
        'carmel':'https://goo.gl/maps/VqZXdhyBNZxTizmw9',
        'stream':'https://goo.gl/maps/nB7yJQzNaukAa9ZN6',
        'midland':'https://goo.gl/maps/XEicjSQPmq7bhuuc9',
        'brk':'https://goo.gl/maps/AVZNKKpusvkeCt529',
        'pebble':'https://goo.gl/maps/j4KiHk79RmHAxB7a9',
        'saturn5':'https://g.page/spacecenterhou?share',
        'cash':'https://www.facebook.com/meowtownar/',
        'cashmace':'https://www.facebook.com/meowtownar/',
    },
    'titles' : {
        'garden':'Boca Chica, TX',
        'maroonbells':'Aspen, CO',
        'starbase':'Starbase, TX',
        'mechazilla':'Boca Chica, TX',
        'carmel':'Monterey Penninsula, CA',
        'stream':'Big Sur, CA',
        'midland':'Midland, TX',
        'brk':'Omaha, NE',
        'pebble':'Monterey Penninsula, CA',
        'saturn5':'Houston, TX',
        'cash':'Fort Worth, TX',
        'cashmace':'Fort Worth, TX',
    },
    'linktext' : {
    },
    'footer':footer,
}