from manim import *


class JWT(Scene):
    def construct(self):
        logo = ImageMobject("../assets/jwt.png")
        self.play(FadeIn(logo))
        self.wait(1)

        code = '''
// Header
{
  "alg": "HS256",   // Algorithm
  "typ": "JWT"      // Token type
}
.
// Payload (Data)
{
  "iss": "https://accounts.google.com",
  "sub": "my.mail@gmail.com",
  "name": "Timo Reusch",
  "exp": 1311281970,    // Expires at
  "iat": 1311280970     // Issued at
}
.
[SIGNATURE]
'''
        rendered_code = Code(code=code, tab_width=4, background="rectangle", insert_line_no=False, style="github-dark",
                             line_spacing=0.8, language="json", font="Monospace", background_stroke_width=0).scale(0.8)\
            .move_to((0, -0.7, 0))
        rendered_code[0].set_z_index(-2)
        self.play(logo.animate.scale(0.5).move_to((0, 3, 0)), FadeIn(rendered_code))
        self.wait(1)

        jwt = '''
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb\n
2dsZS5jb20iLCJzdWIiOiJteS5tYWlsQGdtYW\n
lsLmNvbSIsIm5hbWUiOiJUaW1vIFJldXNjaCI\n
sImV4cCI6MTMxMTI4MTk3MCwiaWF0IjoxMzEx\n
MjgwOTcwfQ
.
_eDawkftqSOvkyADySwf1yBF2iK33jeCC07tG3e85X4
'''
        jwt_rendered = Code(code=jwt, tab_width=4, background="rectangle", insert_line_no=False, style="github-dark",
                             line_spacing=0.8, language="json", font="Monospace", background_stroke_width=0).scale(0.8)\
            .move_to((0, -0.7, 0))
        self.play(Transform(rendered_code, jwt_rendered))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )