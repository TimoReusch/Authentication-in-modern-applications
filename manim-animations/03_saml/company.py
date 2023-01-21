from manim import *


class Company(Scene):
    def construct(self):
        company = SVGMobject(file_name="../assets/company.svg").scale(0.5).move_to((0, 2, 0))
        self.play(FadeIn(company))

        mid = (0, 1.4, 0)
        y = -1.4

        a1 = Arrow(mid, (-3, y, 0))
        a2 = Arrow(mid, (-1, y, 0))
        a3 = Arrow(mid, (1, y, 0))
        a4 = Arrow(mid, (3, y, 0))

        slack = ImageMobject("../assets/slack.png").scale(0.25).move_to((-3, -2, 0))
        self.play(FadeIn(slack), Write(a1))
        sap = ImageMobject("../assets/sap.png").scale(0.2).move_to((-1, -2, 0))
        self.play(FadeIn(sap), Write(a2))
        gitlab = ImageMobject("../assets/gitlab.png").scale(0.5).move_to((1, -2, 0))
        self.play(FadeIn(gitlab), Write(a3))
        zoom = ImageMobject("../assets/zoom.png").scale(0.15).move_to((3, -2, 0))
        self.play(FadeIn(zoom), Write(a4))

        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )