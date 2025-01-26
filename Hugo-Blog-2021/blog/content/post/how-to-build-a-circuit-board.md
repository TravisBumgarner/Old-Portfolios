{
    "title": "How to Build a Circuit Board",
    "date": "2019-04-12T12:05:19-05:00",
    "draft": false,
    "topics": ["writing"],
    "description": "One Day I decided to learn how to make circuit boards. Several months later, my first PCB arried in the mail. This is how I got there.",
    "preview_image": "/image/how-to-build-a-circuit-board/preview_image.jpg"
}

*Note*: This article was originally published to the Painless Prototyping Blog (now deactivated) on November 17th, 2016. 

### Introduction

So you want to build a printed circuit board (PCB)? You’ve come to the right place! These are the steps I took to go from knowing literally nothing about PCBs to having a working product, the Button Board, that I felt was worth selling.


### Breadboarding

Breadboarding is the first step in the process that culminates in a PCB. It’s a chance to sandbox electronics without having to worry about making anything permanent by solder or printing to a circuit board. My journey in electronics started long before I thought of creating my own PCB with the purchase of a [SparkFun Inventor’s Kit](https://www.sparkfun.com/products/12060) which introduced me to the concept of breadboarding. One fascinating epiphany I had along the way is that anything that is possible with a breadboard can be transformed into a PCB.

If you’re thinking about skipping the breadboarding step, stop, trust me. For my first PCB, I decided to do just that and go straight to computer-aided design (CAD). While designing in CAD, I asked an electrical engineering friend, “Would the board work if I did X instead of Y?”, he said yes and instead of testing if it would actually work, I placed an order of PCBs. Three weeks later a package arrived with boards that didn’t work because his answer was wrong.

{{< figure src="/image/how-to-build-a-circuit-board/pcb1.jpg" caption="Breadboarding my Arduino Camera" >}}

### CAD

Now that you have a working circuit on a breadboard, it’s time to convert that into a CAD design that can be then sent off to a manufacturer. [Eagle PCB Design](https://www.autodesk.com/products/eagle/overview) is the standard for the maker community. [Sparkfun](https://github.com/sparkfun/SparkFun-Eagle-Libraries) and many other people have made their libraries of components available so that you don’t have to design them yourself. This allows you to jump right into designing your PCB instead of spending time designing components first.

Jeremy Bloom has a great [three part series](https://www.youtube.com/watch?v=1AXwjZoyNno) on learning Eagle CAD.

Another word of caution is to pay attention to error checking. I didn’t complete this process for V1.1 of the Button Board and ended up with boards that had two wires overlapping which caused some of the buttons not to work properly. If you would like me to take a look at your board, post below. (If your board is for non-commercial use, I would be happy to check it out for free.)

{{< figure src="/image/how-to-build-a-circuit-board/pcb2.png" caption="CAD Model" >}}

### Time to Manufacture!

For my boards, I exclusively use [Dirty PCBs](http://dirtypcbs.com/). The dirty part stands for dirt cheap, not unclean boards. Fellow hackspace members have recommended [PCBShopper](http://pcbshopper.com/) which I have not tried myself.

Dirty PCBs is great because it allows you to upload board (.brd) files from Eagle which is, in my opinion, much simpler than dealing with gerber files. After placing an order, PCBs take between 2 to 3 weeks to arriving. Trust me, the cost savings are well worth it. After receiving your boards, be sure to test them out, get feedback from others, and iterate through the process until you’re happy with your design.

As for components, Ebay is a great place to order cheap components from China. Furthermore, if you opt to use a manufacturer such as DirtyPCBs, the components will arrive about the same time as your PCBs.

{{< figure src="/image/how-to-build-a-circuit-board/pcb3.jpg" caption="Manufactured PCB" >}}

### Stuck somewhere in the process?

Feel free to add a question below and I’ll try and get back to you soon!