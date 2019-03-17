
#based on: https://www.diveinto.org/python3/your-first-python-program.html#importsearchpath
#anaconds search path is apparently incomplete?

# If you are having trouble importing django then fill in and include the below script:
#import sys
#sys.path.insert(0, 'PATH_TO_ANACONDA\\Anaconda3\\envs\\kollab\\Lib\\site-packages')
#sys.path.insert(0, 'PATH_TO_YOUR_PYHON_WORKSPACE\\PythonWorkspace\\kollab_project')

import sys
sys.path.insert(0, 'D:\\Downloads\\Anaconda3\\envs\\kollab\\Lib\\site-packages')
sys.path.insert(0, 'D:\\PythonWorkspace\\PythonWorkspace\\kollab_project')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kollab_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from kollab.models import UserProfile, Tag, Project, Membership
from django.core.files import File
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# Script which simulates typical data we need to save and retrieve

def populate():
    # data which will populate the database
    
    # seperate objects for music and film to seperate some users 
    # and create overlapping interests with other users
    music_tags = [
        {"name" : "Guitar"},
        {"name" : "Bass"} ]
    
    film_tags = [
        {"name" : "Film"},
        {"name" : "Cinematography"},
        {"name" : "Drama"}]
        
    all_tags = [music_tags, film_tags]    
    
    ## generic lorum ipsum style text...in the fashion of Bob Ross
    
    string = "It looks so good, I might as well not stop. Now, we're going to fluff this cloud. Now let's put some happy little clouds in here. If you didn't have baby clouds, you wouldn't have big clouds. We'll put some happy little leaves here and there. Let's make some happy little clouds in our world. A tree cannot be straight if it has a crooked trunk. Without washing the brush, I'm gonna go right into some Van Dyke Brown, some Burnt Umber, and a little bit of Sap Green. If you do too much it's going to lose its effectiveness. This piece of canvas is your world. Let's put a touch more of the magic here. In painting, you have unlimited power. You have the ability to move mountains. Even trees need a friend. We all need friends. We don't really know where this goes - and I'm not sure we really care."
        
    # website used to get lat lon: https://www.mapcoordinates.net/en
    # all lat lons refere to places around glasgow, starting from the centere & going out to dumbarton...dont know why I chose dumbarton...

    hashedPassword = make_password("predictable", salt=None, hasher='default')

    users = [
        {"username" : "Ananya",
         "email": "Ananya@ex.com",
         "password" : hashedPassword},
         {"username" : "Barak",
         "email": "Barak@ex.com",
         "password" : hashedPassword},
         {"username" : "Charlie",
         "email": "Charlie@ex.com",
         "password" : hashedPassword},
         {"username" : "Dav",
         "email": "Dav@ex.com",
         "password" : hashedPassword},
         {"username" : "Ebo",
         "email": "Ebo@ex.com",
         "password" : hashedPassword},
         {"username" : "Faye",
         "email": "Faye@ex.com",
         "password" : hashedPassword},
         {"username" : "Gerry",
         "email": "Gerry@ex.com",
         "password" : hashedPassword},
         {"username" : "Harry",
         "email": "Harry@ex.com",
         "password" : hashedPassword}]
         
    userProfiles =[
         {"selfinfo" : string,
         "picture" : "static/images/pexels-photo-730896.jpg",
         "lat" : 55.87473302,
         "lon" : -4.28724289 },
         {"selfinfo" : string,
         "picture" : "static/images/pexels-photo-759668.jpg",
         "lat" : 55.87473302,
         "lon" : -4.28724289 },
         {"selfinfo" : string,
         "picture" : "static/images/pexels-photo-936006.jpg",
         "lat" : 55.87473302,
         "lon" : -4.28724289 },
         {"selfinfo" : string,
         "picture" : "static/images/pexels-photo-1152854.jpg",
         "lat" : 55.87473302,
         "lon" : -4.28724289 },
         {"selfinfo" : string,
         "picture" : "static/images/pexels-photo-1937301.jpg",
         "lat" : 55.87473302,
         "lon" : -4.28724289 },
         {"selfinfo" : string,
         "picture" : "static/images/pexels-photo-1933873.jpg",
         "lat" : 55.87473302,
         "lon" : -4.28724289 },
         {"selfinfo" : string,
         "picture" : "static/images/pexels-photo-1942037.jpg",
         "lat" : 55.87473302,
         "lon" : -4.28724289 },
         {"selfinfo" : string,
         "picture" : "static/images/pexels-photo-1942037.jpg",
         "lat" : 55.87473302,
         "lon" : -4.28724289 }]
         
    
    projects = [
        {"name": "Magic Music",
         "picture" : "static/images/pexels-photo-1120162.jpg",
         "short": "Music documentory from glasgow",
         "long": "This is your creation - and it's just as unique and special as you are. "},
        {"name": "Weegie Funk Legends",
        "picture" : "static/images/pexels-photo-1813124.jpg",
        "short": "Fusion // Low-Fi // Weegie-Wave",
         "long": "Have fun with it. I spend a lot of time walking around in the woods and talking to trees, and squirrels, and little rabbits and stuff. "},
        {"name": "Taming of the Shew",
        "picture" : "static/images/pexels-photo-1049746.jpg",
        "short": "Glasgow Youth Theater",
         "long": "Automatically, all of these beautiful, beautiful things will happen. Let's have a nice tree right here."}]
    
    preset_memberships_1 = [
        {"user" : users[0]},
        {"user" : users[5]},
        {"user" : users[2]},
        {"user" : users[7]}]
        
    preset_memberships_2 = [
        {"user" : users[4]},
        {"user" : users[7]},
        {"user" : users[1]}]
        
    preset_memberships_3 = [
        {"user" : users[0]},
        {"user" : users[6]},
        {"user" : users[1]}]
        
    memberships = [
        preset_memberships_1,
        preset_memberships_2,
        preset_memberships_3 ]
    
    # iterating through data to functions
    
    for tag in all_tags:
        #print(tag)
        for t in tag:
            #print(t["name"])
            add_tag(t)
    
    for i in range(0, len(users)):
        #print(u)
        add_user(users[i], userProfiles[i])
    
    for p in projects:
        #print(p)
        add_projects(p)
    
    # this loops through memberships and projects and feeds them
    # to add members
    # this loop assumes that the number of preset_membership == num of projects
    for index in range(0,len(projects)):
        for user in memberships[index]:
            add_members(projects[index]['name'], user['user'])
    
    # this is a bit clunky but reflects the need to assign 
    # realistic tags to each project...
    
    # assign music tags to indie band and film tags to drama film
    
    # these loops are trying distribute the tags in a logical way, by theme, they are
    # very 'hacky' and will need to change as we develope the data set
    
    # note range is excluding documentories
    for index in range(1,len(projects)):
        for tag in all_tags[index-1]:
                print(tag)
                add_tags_to_project(projects[index], tag)
    
    ## assign all tags to the documentory project (imagain its a doc about an indy band...to show collaboration / social networking etc)
    for tag in all_tags:
        for t in  tag:
            add_tags_to_project(projects[0], t)
    
    
    for project in Project.objects.all():
        members = project.members.all()
        tags = project.tags.all()
        print(project.name)
        if len(members) < len(tags):
            for tag in range(0, len(tags)):
                #modulo to distribute the tags among members when mem > tags
                index = tag % len(members)
                print(tags[tag])
                print(members[index])
                members[index].tags.add(Tag.objects.filter(name = tags[tag]).first())
        else:
            for mem in range(0, len(members)):
                index = mem % len(tags)
                members[mem].tags.add(Tag.objects.filter(name = tags[index]).first())
                
                
# functions for adding to database


def add_tag(tag):
    # seperating obj/created re docs: https://docs.djangoproject.com/en/2.1/ref/models/querysets/#get-or-create
    obj, created = Tag.objects.get_or_create(name=tag["name"])
    obj.save()
    
# may raise an integrity error if trying to get user thats already been added, just remove them from the data base
def add_user(user, userProfile):
    #obj, created = User.objects.get_or_create(firstName=user['firstName'], lastName=user['lastName'], email=user['email'],lon=user['lon'], lat=user['lat'])
    newuser, created = User.objects.get_or_create(username=user['username'], email=user['email'], password=user['password'])
    newuser.save()
    profile, created = UserProfile.objects.get_or_create(user=newuser)
    profile.lat = userProfile['lat']
    profile.lon = userProfile['lon']
    profile.selfinfo = userProfile['selfinfo']
    profile.picture = File(open(userProfile['picture'], 'rb'))
    profile.save()
    
def add_projects(project):
    obj, created = Project.objects.get_or_create(name=project['name'], short=project['short'], long=project['long'])
    try:
        obj.picture = File(open(project['picture'], 'rb'))
    except Exception:
        print("error")
    obj.save()
    
def add_members(proj, user):
    #print("add members:")
    #print(proj)
    #print(user)    # this = UserProfile.objects.get(user=(User.objects.get(username="test1")))
    obj, created = Membership.objects.get_or_create(userProfile=UserProfile.objects.get(user=User.objects.get(username=user['username'])), project=Project.objects.get(name=proj))
    obj.save()

def add_tags_to_project(proj, tag):
    #print(proj['name'] + "  " + tag['name'])
    project = Project.objects.get(name=proj['name'])
    obj, created = Tag.objects.get_or_create(name=tag['name'])
    obj.save()
    
    project.tags.add(obj)
        
if __name__ == '__main__':
    print("Starting Kollab population script...")
    populate()
         
