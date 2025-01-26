{
    "title": "How to Make a Photo Stitching Website & Avoid Burnout",
    "date": "2020-03-13T16:00:01-04:00",
    "draft": false,
    "topics": ["writing"],
    "description": "Engineers love to start side projects and never finish them. This leads to burnout. Why not build fun things instead? How about a tool to develop virtual cross stitches!",
    "preview_image": "/image/how-to-make-a-photo-stitching-website/preview_image.jpg"
}

<!-- Where to Post
Tweet at https://twitter.com/meowlivia_ and follow
CSS Weekly at https://css-weekly.com/submit-a-link/
Instagram
Twitter
 -->

[Click here to check out the finished result!](https://stitchit.travisbumgarner.com)


### Background

I once read somewhere that burnout is the continued application of large amounts of energy on projects that ultimately end in failure. In the last year or so I've started and failed many projects. To name a few:

- [Winions](https://github.com/TravisBumgarner/winions) - 59 Commits over 1.5 months
- [Watchr](https://github.com/TravisBumgarner/watchr) - 60 Commits over 1 month
- [Make-A-Camera](https://github.com/TravisBumgarner/make-a-camera) - 16 Commits and a fully functioning physical prototype over 6 months
- [Let's Pair](https://github.com/TravisBumgarner/lets-pair) - 139 Commits with a fully functioning application (in need of user testing and refinement) over 6 months

All of these projects were large energy consumers. I kept starting projects, getting tired of the energy demanded, and giving up. 

I had a graveyard full of half completed projects. My love of side projects was inevitably going to lead me to burnout if I maintained this trend. So I decided to do something about it. No more overly complex projects with no end in sight. Instead, I decided to focus on little side projects that would be fun to build and that others might enjoy as well. 

### Motivation

I came across this lovely [CSS Cross Stitch](https://codepen.io/oliviale/pen/RwNdeeQ) of the Pokemon Cyndaquil by [Olivia Ng](https://twitter.com/meowlivia_). (Screenshot of the resulting image below)

{{< figure src="/image/how-to-make-a-photo-stitching-website/motivation.png" caption="Project Motivation" >}}

### A little bit more background...

To make sharing my fun projects with the world - I decided it was time for new hosting. After talking with a devops engineering coworker I decided to go with Google Cloud Platform. I knew almost nothing about it but figured it was time to learn. This project would be my first larger endeavor. 

### So I dove right in...

I banged my head against the wall, a lot. I tried to keep track of all the resources that I used but in the end gave up. Here is what just one day of my browsing history for "Google Cloud Platform" looked like:

{{< figure src="/image/how-to-make-a-photo-stitching-website/somanylearnings.png" caption="Lots to Learn" >}}

The above image goes to show that even with several years of experience, I'm still Googling lots of things.

I am super grateful to the developer community and was able to keep track of some of the more influential/helpful/inspirational pages I found:

- [Stack Overflow](https://stackoverflow.com/a/43111221) - A great answer on how to find interesting colors in an image.
- [PyImageSearch](https://www.pyimagesearch.com/) - A great website on everything computer vision related.
- [Hosting Flask servers on Firebase from scratch](https://medium.com/firebase-developers/hosting-flask-servers-on-firebase-from-scratch-c97cfb204579) - Everything you need to get started deploying sites more complicated than static pages to GCP.
- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) - Everything you need to know to get up and running with Flask.

### How It Works - The Architecture

{{< figure src="/image/how-to-make-a-photo-stitching-website/architecture.png" caption="Architecture" >}}

#### Preface

Everything related to GCP in this project was brand new to me. I used to develop with Flask but had to go read some refersher content. 

#### Diving into the Architecture

There are three intersting journeys here, denoted by the three circles.

##### 1. Deploying Code

The Flask and Firebase article I mentioned above helped with this first part. 

Cloud Build and Cloud Run are tools that collectively took the code off my machine, created a Docker image with it, and sent it to GCP so that users could access the site. 

##### 2. Accessing the Stitching Tool

The end user gets a webpage where they can enter a photo. That photo goes off to the API which is powered by Flask. Flask sends the photo to my stitch_image function and returns the resulting CSS to the user.

##### 3. Avoiding a giant Bill

I have been rather fearful of racking up a large bill with this project. I setup a little trigger here that when my bill passes a certain threshold, I get a message to phone telling me so. 

### How it Works - The Algorithm

I've scattered comments throughout the code below. 

```multiline
# 1. Read image from file upload
npimg = np.frombuffer(filestr, np.uint8)
img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)

# 2. Resize image and handle various file types
img = imutils.resize(img, width=1000)
img = imutils.resize(img, height=1000)
input_width, input_height, *_ = img.shape

if len(img.shape) > 2 and img.shape[2] == 4:
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

sample_size = round(input_width / horizontal_samples_user_input)
vertical_samples = round(input_height / sample_size)

# 3. Create the output HTML string that will hold all of the resulting CSS image
output_html = ''

output_html += '\t\t<div id="wrapper"><div id="image">\n'

# 4. Iterate over the image, left to right, top to bottom, in small sections.
for i in range(0, horizontal_samples_user_input):
    output_html += '\t\t\t<div class="row">\n'
    
    for j in range(0, vertical_samples):
        i_start = i*sample_size
        i_end = i*sample_size+sample_size
        j_start = j*sample_size
        j_end = j*sample_size+sample_size

        # 5. See below for kmeans_image()
        b,g,r = kmeans_image(img[i_start:i_end, j_start:j_end])
        output_html += f'\t\t\t\t<div style="background-color: rgb({r},{g},{b});" class="cell">'
        output_html += '</div>\n'
    
    output_html += '\t\t\t</div>\n'

# 7. The HTML string is returned back to Flask to send to the user. 
output_html += '\t\t</div></div>\n'
return output_html


# 6. If you just took the average RGB values in a given section of an image, you
# would probably just end up with gray or brown. K Means clustering is a way to 
# look at all the colors in three dimensional space - red one axis, green the next
# blue the last and trying to group similar RGB values together and then take their
# averages locally. This results in much more interesting colors. Read the Stack Overflow 
# link above to learn more. 
def kmeans_image(img):
    pixels = np.float32(img.reshape(-1, 3))

    n_colors = 3
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)

    return np.uint8(palette[-1])
```

### How does it look?

I've taken a few of my own photographs and run them through. 

{{< figure src="/image/how-to-make-a-photo-stitching-website/result1.png" caption="Result 1" >}}

{{< figure src="/image/how-to-make-a-photo-stitching-website/result2.png" caption="Result 2" >}}

{{< figure src="/image/how-to-make-a-photo-stitching-website/result3.png" caption="Result 3" >}}

### Call to Action

Have you created any cool cross stitchings? Share them below!