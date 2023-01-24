from manim import *


class Sources(Scene):
    def construct(self):
        source = Text("12", font_size=12).move_to((-6.6, -3.6, 0))
        circle = Circle(color=DARK_BLUE, fill_opacity=0.5).surround(source, buffer_factor=2)
        group = Group(source, circle)
        self.play(FadeIn(group, shift=0.2*UP))
        self.wait(2)
        self.play(FadeOut(group, shift=0.2*DOWN))