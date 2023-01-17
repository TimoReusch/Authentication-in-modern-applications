from manim import *


class Company(Scene):
    def construct(self):
        company = SVGMobject(file_name="assets/company.svg").scale(0.5).move_to((0, 2, 0))
        self.play(FadeIn(company))

        mid = (0, 1.4, 0)
        y = -1.4

        a1 = Arrow(mid, (-3, y, 0))
        a2 = Arrow(mid, (-1, y, 0))
        a3 = Arrow(mid, (1, y, 0))
        a4 = Arrow(mid, (3, y, 0))

        slack = ImageMobject("assets/slack.png").scale(0.25).move_to((-3, -2, 0))
        self.play(FadeIn(slack), Write(a1))
        sap = ImageMobject("assets/sap.png").scale(0.2).move_to((-1, -2, 0))
        self.play(FadeIn(sap), Write(a2))
        microsoft = ImageMobject("assets/microsoft.png").scale(0.1).move_to((1, -2, 0))
        self.play(FadeIn(microsoft), Write(a3))
        gitlab = ImageMobject("assets/gitlab.png").scale(0.5).move_to((3, -2, 0))
        self.play(FadeIn(gitlab), Write(a4))
