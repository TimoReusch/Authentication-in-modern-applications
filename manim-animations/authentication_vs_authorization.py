from manim import *


class AuthenticationVsAuthorization(Scene):
    def construct(self):
        test = "a", "b", "c"
        auth = BulletedList(test, height=2, width=2)
        self.play(FadeIn(auth))
