{
    "title": "Combining Hobbies: Programming, Electronics & Photography",
    "date": "2016-04-04T09:00:00-00:00",
    "draft": false,
    "topics": ["writing"],
    "preview_image": "/image/combining-hobbies/preview_image.jpg",
    "description": "This is an exploration into learning more about photography by building a camera."
}

*Note*: This article was originally published in three parts to my Photography Portfolio Blog in 2016. 

# Part 1

At some point several weeks ago I set about brainstorming what new project I wanted to work on. I scribbled out subjects I had experience with or wanted to learn about and I ended up drawing circles around programming, electronics, and photography as a good combination. I knew nothing of programming, just a little bit about electronics, and probably an unhealthy amount about photography.

<!--more-->

{{< highlight cpp >}}
while True {
    turnOn(LED)
    wait(1)
    turnOff(LED)
    wait(1)
}
{{< /highlight >}}

I like to use the [Arduino](http://arduino.cc) for electronics because it's really easy to use. The computer code to make a LED blink is as simple as the code to the left.

{{< figure src="/image/combining-hobbies/arducam.jpg" caption="Arducam" >}}

I then set about trying to find a camera that would plug into the Arduino and found the [Arducam](http://arducam.com]). A $30, 2 megapixel camera that, along with an SD card reader, could offer the basic features of a camera, shoot and save, along with some settings adjustments such as image size and white balance.

So now that I had a camera to play with, what to do with it? With some more brainstorming I decided I'd create time lapse images of single scenes. Not a video, but a single image to demonstrate the passing of time. The left side of the image represents the start of the photo capturing period and the right side the end.

This would be achieved with the camera set in a location and set to run for a given period of time. The images would then be taken off the SD card and loaded into a Python programming script. To easily demonstrate this I'll explain by stitching three images. A cut of the left third of the first image, a cut from the middle third of the second image, and a cut from the right third of the last image, are then stitched together into a final image. I've written a script, which can be viewed on [Github](https://github.com/TravisBumgarner/PhotoStitch), that can take any number of images and stitch them together. Below is a test with fake input images of solid colors representing a sunrise over time, the script running, and the output.

{{< figure src="/image/combining-hobbies/example.png" caption="Example Output" >}}

Next time, I'll share more about the electronics, Arduino programming, test results, and quality improvements.

# Part 2

While I waited for the Arducam camera to arrive I set about designing the user display/inputs. After a bunch of sketching, I narrowed my setup to include an 16x2 LCD screen and 4 input buttons. I also brainstormed the settings I wanted to control. You can see the setup in action below.

I ran into a flash memory issue where I ran out of space on the Arduino chip. I have two implementations of this project, one to control the little Arducam camera, and another to control a DSLR. Once I create the design for the DSLR, I can remove the SD card reader and Arducam which will free up a bunch of flash memory which will allow me to add more custom settings. Until then, I've had to keep it simple.

{{< youtube TFMe69kptv0 >}}

Once the camera arrived, I rewrote the code to include the ArduCam library. This is about the point where I began to lose my mind a bit. I pushed the flash memory to its limit with libraries for an LCD screen, SD Card reader, and Arducam.  This started to cause some errors I couldn't quite figure out. In the end, I had to take a break to figure out how to clean up my code and reduce its size. When you're working with an Arduino, you only have 16KB which runs out quite quickly. After several hours of coding issues as well as some physical wiring issues, I had a working camera!

{{< youtube xecbKr4nb_E >}}

With a working camera, it was time for tests. I kept having partial successes leaving my camera running and taking pictures. However, 1 in every 15 or so images wouldn't save properly and the camera wouldn't always continually run. After several hours of troubleshooting issues, I realized that the SD card had reached its end and since I only had one, I've had to take a break while I wait for a new card. I was able to run a successful test of taking pictures with the camera, exporting them to the computer, and modifying them with the Python script I wrote.

{{< figure src="/image/combining-hobbies/finalImage0-1.png" caption="Sample Output" >}}

It's not the most beautiful view but you can see the passage of time in this stitched image. If you look at the wood fence near the car, towards the left side is when the sun wasn't out but as you move towards the right, the fence gets brighter. That's where the sun came out for a few minutes.

There's still work to be done but I've gained a lot of feedback from my tests and now have some new stuff to work on. I'll be back when I have another update. Next time I'll have a bit to say about simplifying/finalizing the circuit, hooking up a DSLR, and more test images.

# Part 3

For better or worse, I made the decision to jump right into soldering as my next step with my camera. I'd soldered before but never to such a great extent with an end goal in mind. I began by arranging the components with ease of access/sight of the buttons and screen. I then, very slowly/painfully set about soldering everything. After roughly 7 - 10 hours I'd soldered everything together.

Some lessons learned:
* Perfboards suck, go with stripboards. But then, perfboards suck, make a PCB. That'll be one of my next steps in this whole learning electronics journey.
* Do not solder under low light or for several hours at once. Also, like they say in carpentry to measure twice and cut once, place your pins/wires/components twice and solder once.

{{< figure src="/image/combining-hobbies/arducam3-1-1.jpg" caption="Saturday Night Soldering" >}}

{{< figure src="/image/combining-hobbies/arducam3-1-2.jpg" caption="Sunday Morning Soldering" >}}

{{< figure src="/image/combining-hobbies/arducam3-1-3.jpg" caption="Finished Bottom Shot" >}}

{{< figure src="/image/combining-hobbies/arducam3-1-4.jpg" caption="Finished Top Shot" >}}

Next step was to consider the housing. I have access to a laser cutter and CNC machine but for the time being, decided on a very rudimentary housing with some screws, nuts, and wood. I just purchased a 3D printer so I might revisit case design at a future date. For now this is where the project will take a pause since I already have an idea for a version 2 of this whole project.

{{< figure src="/image/combining-hobbies/arducam3-1-5.jpg" caption="Finished Project!" >}}

Time to head out and shoot some cooler pictures.

For now, enjoy a typical timelapse shot I took from my kitchen window.  Just an FYI, it is of terrible quality, I know. I was more focused on just getting the thing to work, the next step will be learning how to take good pictures with my new camera.  Also, the jerkiness is due to my roommates/pets/me bumping into the camera. (Another design consideration!)

{{< youtube yd60Sxf1P1o >}}