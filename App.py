import kivy
from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.graphics import Color, Rectangle
# from kivy.properties import NumericProperty, ObjectProperty, ReferenceListProperty            
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.core.window import Window
kivy.require("1.0.9")


'''
Optimize imports later
'''
# def animate_image(self, *args, **kwargs):
#     image_animate = Animation()

#     def f(i, w):
#         w.source = 'image%d.jpg' % i

#     for i in range(4):

#         a = Animation(x = (i + 10), duration=(0.10 * i),
#                       )
#         a.on_complete = functools.partial(f, i)


#         image_animate += a

#     image_animate.start(self.anim_image)
#     

def InitPane(Screen):
    pass

def MainPane(Screen):
    pass

def RootPane(ScreenManager):
    pass





class LogoAnimation(Widget):
    image_animate = Animation()
    i = 0
    image_animate += Animation(x = 250, y = 250, image_num=i, duration=(0.10 * i))

class Cursor(Image):
    def __init__(self, **kwargs):
        super(Cursor, self).__init__(**kwargs)
        self.source = 'crosshair.png'
        self.size = (10,10)        
        Widget.size_hint = None, None
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, input_type='text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)



class InitialScreen(Widget):
    layout = AnchorLayout( anchor_x='right', anchor_y='bottom' )
    i = 0
    Widget.size(880, 650)
    Widget.size_hint = (None, None)
    anim = Animation(x=100, y=100)
    anim.start(LogoAnimation)
    def draw_background(self, *args):
        Widget.canvas.before.clear()
        with Widget.canvas.before:
            Color(.4, .4, .4, 1)
            i = 1
            texture = CoreImage(("image%d.png") % i).texture
            texture.wrap = 'repeat'
            nx = float(Widget.width) / texture.width
            ny = float(Widget.height) / texture.height
            Rectangle(pos=Widget.pos, size=Widget.size, texture=texture,
                    tex_coords=(0, 0, nx, 0, nx, ny, 0, ny))


class ManGUINet(App):
    def build(self):
        pane1 = InitialScreen()
        return pane1


if __name__ == '__main__':
    ManGUINet().run()
