from manim import *


class Sso(Scene):
    def construct(self):
        font_size = 22

        company = SVGMobject(file_name="../assets/company.svg").scale(0.5).move_to((0, 2, 0))

        mid = (0, 1.4, 0)
        y = -1.4

        a1 = Arrow(mid, (-3, y, 0))
        a2 = Arrow(mid, (-1, y, 0))
        a3 = Arrow(mid, (1, y, 0))
        a4 = Arrow(mid, (3, y, 0))

        slack = ImageMobject("../assets/slack.png").scale(0.25).move_to((-3, -2, 0))
        sap = ImageMobject("../assets/sap.png").scale(0.2).move_to((-1, -2, 0))
        gitlab = ImageMobject("../assets/gitlab.png").scale(0.5).move_to((1, -2, 0))
        zoom = ImageMobject("../assets/zoom.png").scale(0.15).move_to((3, -2, 0))
        self.play(FadeIn(company), FadeIn(slack), FadeIn(a1), FadeIn(sap), FadeIn(a2), FadeIn(gitlab), FadeIn(a3),
                  FadeIn(zoom), FadeIn(a4))

        self.wait(1)

        self.play(FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(a4), FadeOut(slack), FadeOut(zoom), FadeOut(gitlab),
                  FadeOut(company), sap.animate.move_to((-4, 0, 0))
                  )

        self.wait(1)

        # Service Provider
        sp = Text("Service Provider", font_size=font_size).next_to(sap, DOWN)
        sp_box = SurroundingRectangle(Group().add(sap, sp), color=BLUE, buff=MED_SMALL_BUFF)

        # Identity provider
        company = SVGMobject("../assets/company.svg").scale(0.4).move_to((4, 0, 0))
        idp = Text("Identity Provider", font_size=font_size).next_to(company, DOWN)
        idp_box = SurroundingRectangle(Group().add(company, idp), color=GREEN, buff=MED_SMALL_BUFF)
        self.play(Create(sp), Create(sp_box), FadeIn(company), Create(idp), Create(idp_box))

        self.wait(1)

        # Arrow: Service provider -> Identity provider
        authentication_request_arrow = Arrow((-2.5, 0, 0), (2.5, 0, 0))
        authentication_request = Text("Authentication Request", font_size=font_size) \
            .next_to(authentication_request_arrow, UP)
        self.play(Create(authentication_request_arrow), FadeIn(authentication_request))

        self.wait(1)

        # Arrow: Identity provider -> Service provider
        authentication_assertion_arrow = Arrow((2.5, -0.5, 0), (-2.5, -0.5, 0))
        authentication_assertion = Text("Authentication Assertion", font_size=font_size) \
            .next_to(authentication_assertion_arrow, DOWN)
        self.play(Create(authentication_assertion_arrow), FadeIn(authentication_assertion))

        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )