from .contentWords import wordsuco, wordsund, wordsuca, wordsem, wordsHome

# Common stuff
#######

techdict = {
        'python':{'icon':'static/icons/python.svg', 'name':'Python', 'link':'https://www.python.org'},
        'javascript':{'icon':'static/icons/javascript.svg', 'name':'JavaScript (JS)', 'link':'https://developer.mozilla.org/en-US/docs/Web/JavaScript'},
        'sql':{'icon':'static/icons/sql.svg','name':'PostgreSQL', 'link':'https://www.postgresql.org'},
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
    }

footer = {
    'techlist':['python','flask', 'bulma'],
    'techdict': techdict,
    'deployed':'heroku',
}


# pages
#######
projects = {
    'title':'Projects',
    'quote':"""
    Stay primitive. Trust the soup. Swing for the seats. Be ready for resistance. - Steven Pressfield
    """,
    'projects':{
        'stockmarket':{
            'title':'The Stock Market',
            'images':'static/stockmarket.png',
            'words':['blah blah blah','blah blah blah', 'blah blah blah'],
            'techlist':['python','flask','bootstrap'],
            'techdict': techdict,
            'link':'https://lit-eyrie-84189.herokuapp.com'
        },
        'project2':{
            'title':'Project Two',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['javascript','django','bulma'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
        'project3':{
            'title':'Project Three',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['github','heroku','sql'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
        'project4':{
            'title':'Project Four',
            'images':'static/stockmarket.png',
            'words':['blah blah blah','blah blah blah', 'blah blah blah'],
            'techlist':['python','flask','bootstrap'],
            'techdict': techdict,
            'link':'https://lit-eyrie-84189.herokuapp.com'
        },
        'project5':{
            'title':'Project Two',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['javascript','django','bulma'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
        'project6':{
            'title':'Project Three',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['github','heroku','sql'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
        'project7':{
            'title':'The Stock Market',
            'images':'static/stockmarket.png',
            'words':['blah blah blah','blah blah blah', 'blah blah blah'],
            'techlist':['python','flask','bootstrap'],
            'techdict': techdict,
            'link':'https://lit-eyrie-84189.herokuapp.com'
        },
        'project8':{
            'title':'Project Two',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['javascript','django','bulma'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
        'project9':{
            'title':'Project Three',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['github','heroku','sql'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
    },
    'footer':footer
}



home = {
    'title': 'Welcome',
    'quote': {
        'welcome': """
        "The fight is won or lost far away from witnesses - behind the lines, in the gym, and out there on the road, long before I dance under those lights." - Muhammad Ali'
        """,
        'skills': """
        “What looks like talent is often careful preparation. What looks like skill is often persistent revision.” - James Clear
        """,
        'learn':"""
        "You can't connect the dots looking forward; you can only connect them looking backward..." - Steve Jobs
        """
    },
    'words': wordsHome,
    'icons': {
        'python':{'icon':'static/icons/python.svg', 'name':'Python', 'link':'https://www.python.org'},
        'javascript':{'icon':'static/icons/javascript.svg', 'name':'JavaScript (JS)', 'link':'https://developer.mozilla.org/en-US/docs/Web/JavaScript'},
        'sql':{'icon':'static/icons/sql.svg','name':'PostgreSQL', 'link':'https://www.postgresql.org'},
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
    },
    'university':{
        'uco':{'images':'static/uco.png', 'title':'University of Colorado', 'words': wordsuco, 'link':'https://colorado.edu'},
        'und':{'images':'static/und.png', 'title':'University of Notre Dame', 'words': wordsund, 'link':'https://www.nd.edu'},
        'em':{'images':'static/em.png', 'title':'ExxonMobil', 'words': wordsem, 'link':'https://www.exxonmobil.com'},
        'uca':{'images':'static/uca.png', 'title':'University of California, Berkeley Extension', 'words': wordsuca, 'link':'https://extension.berkeley.edu'},
        
    },
    'footer': footer
}



fun = {
    'title':'Interests',
    'quote' : """
    "Curiosity has its own reason for existing."\n\t- Albert Einstein
    """,
    'locs' : ['maroonbells', 'stream', 'mechazilla','garden', 'starbase','saturn5', 'midland', 'brk', 'pebble', 'carmel'],
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
    },
    'words' : {
        'garden':["This is the SpaceX 'Rocket Garden' at Starbase where the older rockets are on display for the public.  It is incredible how close you can get.", "This was such a fun experience wondering through the SpaceX facility and seeing all the progress they have made in such a short amount of time."],
        'maroonbells':["This is a picture of the famous 'Marroon Bells' near Aspen, CO.", "Having grown up in Colorado I'll always love and appreciate the beauty of the mountains especially in the summertime."],
        'starbase':["Starbase Texas, where SpaceX is developing the rockets and technology to go to Mars. It's remarkable what they are doing down at the end of Texas.", "The 'Starbase' is becoming a popular tourist stop in Texas. The top of this long sign is tiled in solar panels."],
        'mechazilla':["This is a view from Boca Chica Beach looking back at the SpaceX launch complex.", "The launch and catch structure has been nicknamed 'Mechazilla' is a sight to see.", "In the picture you can also see a heavy booster and a 'Starship'."],
        'carmel':["The California coast is a remarkable site and the Monterey penninsula is beautiful place.", "In this picture you can see a part of the famous Pebble Beach golf course."],
        'stream':["In Pfieffer Big Sur State Park we were surrounded by giant redwoods and sequoias (although there aren't any in this photo).", "The trees are indescribable, not to mention hard to capture in a photograph...", "Some day I hope to get up to Redwood National Park."],
        'midland':["In 2015 at ExxonMobil I was assigned to be the analyst for the West Texas business unit.", "During this time, the United States became the largest oil producer in the world overtaking Saudia Arabia and Russia.  Driven by the renaissance of oil production in West Texas", "This is view is the oil fields as you fly into Midland and the image left a strong impression on me to this day."],
        'brk':["Studying the writings of Warren Buffett has been one of the most import steps in my development as a business professional.", "In 2016 I decided to attend the Berkshire Hathaway Annual meeting.", "Simply remarkable to think a textile company has been turned into what Berkshire Hathaway is today without any additional outside capital."],
        'pebble':["Another stunning view of the California coast...the loan cypress.","The ocean is stunning, even with less than ideal weather on a day like this",],
        'saturn5':["If you are in Texas and you are interested in the space then the Johnson Space Center near Houston is a must see.", "On display here is a Saturn V rocket cobbled together with remaining parts from the Apollo missions.", "This rocket is massive!"],
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
    },
    'linktext' : {
    },
    'footer':footer,
}

contact = {
    'k': ['linkedin', 'email', 'github', 'twitter'],
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