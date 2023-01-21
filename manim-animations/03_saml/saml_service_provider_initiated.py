from manim import *


class Saml(Scene):
    def construct(self):
        font_size = 22

        company = SVGMobject(file_name="../assets/company.svg").scale(0.5).move_to((0, 2, 0))
        self.play(FadeIn(company))

        self.wait(1)

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

        self.play(FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(a4), FadeOut(slack), FadeOut(sap), FadeOut(gitlab),
                  FadeOut(company), zoom.animate.move_to((-5, 0, 0))
                  )

        self.wait(1)

        # Service Provider
        # zoom = ImageMobject("assets/zoom.png").scale(0.1).move_to((-5, 0, 0))
        sp = Text("Service Provider", font_size=font_size).next_to(zoom, DOWN)
        sp_box = SurroundingRectangle(Group().add(zoom, sp), color=BLUE, buff=MED_SMALL_BUFF)
        self.play(Create(sp), Create(sp_box))

        self.wait(1)

        # Identity provider
        company = SVGMobject("../assets/company.svg").scale(0.4).move_to((2, 0, 0))
        idp = Text("Identity Provider", font_size=font_size).next_to(company, DOWN)
        idp_box = SurroundingRectangle(Group().add(company, idp), color=GREEN, buff=MED_SMALL_BUFF)
        self.play(FadeIn(company), Create(idp), Create(idp_box))

        self.wait(1)

        # User
        craig = ImageMobject("../assets/user.png").scale(0.3).move_to((-5, 1.2, 0))
        self.play(FadeIn(craig))

        self.wait(1)

        # Arrow: Service provider -> Identity provider
        authentication_request_arrow = Arrow((-3.5, 0, 0), (0.5, 0, 0))
        authentication_request = Text("Authentication Request", font_size=font_size) \
            .next_to(authentication_request_arrow, UP)
        self.add_foreground_mobjects(craig)
        self.play(Create(authentication_request_arrow), FadeIn(authentication_request), craig.animate.move_to((1, 0.5, 0)))

        self.wait(1)

        # Arrow: Identity provider -> Login
        arrow_login = Arrow((2, 0.7, 0), (3.8, 2.5, 0))
        arrow_login_text = Text("Show login", font_size=font_size).next_to(arrow_login, LEFT)
        # Login
        login = ImageMobject("../assets/login.png").scale(0.4).move_to((5, 2.5, 0))
        self.play(Create(arrow_login), FadeIn(arrow_login_text), FadeIn(login), craig.animate.move_to((3.4, 3, 0)))

        self.wait(1)

        # Arrow: Login -> User repository
        arrow_db = Arrow((5, 1.3, 0), (5, -2, 0))
        validate = Text("Validate\ncredentials", font_size=font_size).next_to(arrow_db, RIGHT)
        self.play(Create(arrow_db), FadeIn(validate))

        self.wait(1)

        # User repository
        db = SVGMobject("../assets/database.svg").scale(0.4).move_to((5, -2.5, 0))
        info_db = Text("User Repository", font_size=font_size).next_to(db, DOWN)
        self.play(FadeIn(db), Write(info_db))

        self.wait(1)

        # Arrow: User repository -> Identity provider
        arrow_repo = Arrow((3.8, -3, 0), (2, -1.2, 0))
        verification_response = Text("Verification\nresponse", font_size=font_size).next_to(arrow_repo, LEFT)
        self.play(Create(arrow_repo), FadeIn(verification_response))

        self.wait(1)

        # Arrow: Identity provider -> Service provider
        authentication_assertion_arrow = Arrow((0.5, -0.5, 0), (-3.5, -0.5, 0))
        authentication_assertion = Text("Authentication Assertion", font_size=font_size)\
            .next_to(authentication_assertion_arrow, DOWN)
        self.play(Create(authentication_assertion_arrow), FadeIn(authentication_assertion),
                  craig.animate.move_to((-5, 1.2, 0)))

        self.wait(1)

        title = Text("Service Provider-Initiated SSO", font_size=27, weight=BOLD).move_to((-4, 3, 0))
        self.play(Write(title))

        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )