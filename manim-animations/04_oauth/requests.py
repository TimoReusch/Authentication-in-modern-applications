from manim import *


class AuthRequest(Scene):
    def construct(self):
        code = '''GET

https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?
    client_id=92374673
    &scope=email openid https://www.googleapis.com/auth/contacts.readonly
    &response_type=code
    &redirect_uri=https://account.proton.me/oauth/callback
    [...]
'''
        rendered_code = Code(code=code, tab_width=4, background="rectangle", insert_line_no=False, style="github-dark",
                             line_spacing=0.8, language="python", font="Monospace", background_stroke_width=0).scale(0.8)
        rendered_code[0].set_z_index(-2)

        self.play(FadeIn(rendered_code))

        highlights = [None]
        FadeIn(highlights[0])
        self.wait(1)

        counter = 1
        for x in range(3, 7):
            highlights.append(BackgroundRectangle(rendered_code[2][x][1:], buff=0.05, stroke_width=1, color=GREEN, fill_opacity=0.5, z_index=-1))
            self.play(FadeOut(highlights[counter-1]), Create(highlights[counter]))
            counter += 1
            self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class CodeResponse(Scene):
    def construct(self):
        code = '''GET
        
https://account.proton.me/oauth/callback?
    state=proton-web-1f81b885-1fac-c94f-a7de-972e83a74042
    &code=N5VEXnrzd6_dRdQAZkPiQCyvokAr7R7WpvpY32T2
    &scope=email https://www.googleapis.com/auth/contacts.readonly openid
    &authuser=0
    &prompt=consent
'''
        rendered_code = Code(code=code, tab_width=4, background="rectangle", insert_line_no=False, style="github-dark",
                             line_spacing=0.8, language="python", font="Monospace", background_stroke_width=0).scale(0.8)
        rendered_code[0].set_z_index(-2)

        self.play(FadeIn(rendered_code))
        highlight = BackgroundRectangle(rendered_code[2][4][1:], buff=0.05, stroke_width=1, color=GREEN, fill_opacity=0.5, z_index=-1)
        self.play(Create(highlight))
        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class TokenExchange(Scene):
    def construct(self):
        code = '''POST

www.googleapis.com/oauth2/v4/token 
Content-Type: application/x-www-form-urlencoded

code=N5VEXnrzd6_dRdQAZkPiQCyvokAr7R7WpvpY32T2
&client_id=92374673
&client_secret=strengGeheim123
&grant_type=authorization_code        
'''
        rendered_code = Code(code=code, tab_width=4, background="rectangle", insert_line_no=False, style="github-dark",
                             line_spacing=0.8, language="python", font="Monospace", background_stroke_width=0).scale(0.8)
        rendered_code[0].set_z_index(-2)

        self.play(FadeIn(rendered_code))
        highlight1 = BackgroundRectangle(rendered_code[2][2], buff=0.05, stroke_width=1, color=GREEN, fill_opacity=0.5, z_index=-1)
        self.play(Create(highlight1))
        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        self.play(FadeIn(rendered_code))
        highlight2 = BackgroundRectangle(rendered_code[2][7], buff=0.05, stroke_width=1, color=GREEN, fill_opacity=0.5, z_index=-1)
        self.play(Create(highlight2))
        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class TokenResponse(Scene):
    def construct(self):
        code = '''
{
  "access_token": "aEHcyKhkL6FLSWJwiYoD3dMRN2e4bY",
  "expires_in": 3920,
  "token_type": "Bearer"
}
'''
        rendered_code = Code(code=code, tab_width=2, background="rectangle", insert_line_no=False, style="github-dark",
                             line_spacing=0.8, language="json", font="Monospace", background_stroke_width=0).scale(0.8)
        rendered_code[0].set_z_index(-2)

        self.play(FadeIn(rendered_code))
        self.wait(1)

        highlight = BackgroundRectangle(rendered_code[2][1][2:], stroke_width=1, buff=0.05, color=GREEN, fill_opacity=0.5, z_index=-1)
        self.play(Create(highlight))

        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class RequestWithBearer(Scene):
    def construct(self):
        code = '''
GET people.googleapis.com
Authorization: Bearer aEHcyKhkL6FLSWJwiYoD3dMRN2e4bY        
'''
        rendered_code = Code(code=code, tab_width=2, background="rectangle", insert_line_no=False, style="github-dark",
                             line_spacing=0.8, language="python", font="Monospace", background_stroke_width=0).scale(0.8)
        rendered_code[0].set_z_index(-2)

        self.play(FadeIn(rendered_code))
        self.wait(1)

        highlight = BackgroundRectangle(rendered_code[2][1], stroke_width=1, buff=0.05, color=GREEN, fill_opacity=0.5, z_index=-1)
        self.play(Create(highlight))

        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class RequestToken(Scene):
    def construct(self):
        code = '''GET

https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?
	client_id=92374673
	&scope=email openid https://www.googleapis.com/auth/contacts.readonly
	&response_type=code
	&redirect_uri=https://account.proton.me/oauth/callback
	[...]
'''
        rendered_code = Code(code=code, tab_width=4, background="rectangle", insert_line_no=False, style="github-dark",
                             line_spacing=0.8, language="python", font="Monospace", background_stroke_width=0).scale(0.8)
        rendered_code[0].set_z_index(-2)

        self.play(FadeIn(rendered_code))
        self.wait(1)

        highlight = BackgroundRectangle(rendered_code[2][5][1:], stroke_width=1, buff=0.05, color=GREEN, fill_opacity=0.5, z_index=-1)
        self.play(Create(highlight))

        self.wait(2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )