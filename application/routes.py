"""
Using redirect route instead of simple routes since it supports strict_slash
Simple route: http://webapp-improved.appspot.com/guide/routing.html#simple-routes
RedirectRoute: http://webapp-improved.appspot.com/api/webapp2_extras/routes.html#webapp2_extras.routes.RedirectRoute
"""

from webapp2_extras.routes import RedirectRoute
import handlers

secure_scheme = 'https'

_routes = [
    RedirectRoute('/about/', handlers.AboutHandler, name='about', strict_slash=True),
    RedirectRoute('/taskqueue-send-email/', handlers.SendEmailHandler, name='taskqueue-send-email', strict_slash=True),
    RedirectRoute('/_ah/login_required', handlers.LoginRequiredHandler),
    RedirectRoute('/login/', handlers.LoginHandler, name='login', strict_slash=True),
    RedirectRoute('/logout/', handlers.LogoutHandler, name='logout', strict_slash=True),
    RedirectRoute('/social_login/<provider_name>', handlers.SocialLoginHandler, name='social-login', strict_slash=True),
    RedirectRoute('/social_login/<provider_name>/complete', handlers.CallbackSocialLoginHandler,
                  name='social-login-complete', strict_slash=True),
    RedirectRoute('/social_login/<provider_name>/delete', handlers.DeleteSocialProviderHandler,
                  name='delete-social-provider', strict_slash=True),
    RedirectRoute('/register/', handlers.RegisterHandler, name='register', strict_slash=True),
    RedirectRoute('/activation/<user_id>/<token>', handlers.AccountActivationHandler, name='account-activation',
                  strict_slash=True),
    RedirectRoute('/resend/<user_id>/<token>', handlers.ResendActivationEmailHandler, name='resend-account-activation',
                  strict_slash=True),
    RedirectRoute('/contact/', handlers.ContactHandler, name='contact', strict_slash=True),
    RedirectRoute('/settings/profile', handlers.EditProfileHandler, name='edit-profile', strict_slash=True),
    RedirectRoute('/settings/password', handlers.EditPasswordHandler, name='edit-password', strict_slash=True),
    RedirectRoute('/settings/email', handlers.EditEmailHandler, name='edit-email', strict_slash=True),
    RedirectRoute('/password-reset/', handlers.PasswordResetHandler, name='password-reset', strict_slash=True),
    RedirectRoute('/password-reset/<user_id>/<token>', handlers.PasswordResetCompleteHandler,
                  name='password-reset-check', strict_slash=True),
    RedirectRoute('/change-email/<user_id>/<encoded_email>/<token>', handlers.EmailChangedCompleteHandler,
                  name='email-changed-check', strict_slash=True),
    RedirectRoute('/contest', handlers.ContestHandler, name="contest", strict_slash=True),
    RedirectRoute('/game', handlers.GameHandler, name="game", strict_slash=True),
    RedirectRoute('/course/learn/viewer', handlers.LearnHandler, name="learn", strict_slash=True),
    RedirectRoute('/practise', handlers.PractiseHandler, name="learn", strict_slash=True),
    RedirectRoute('/contest/result', handlers.ResultContestHandler, name='result-contest', strict_slash=True),
    RedirectRoute('/contest/result/user', handlers.ResultContestUserHandler, name='result-contest-user', strict_slash=True),
    #RedirectRoute('/info', handlers.InfoHandler, name='info', strict_slash=True),
    RedirectRoute('/dashboard', handlers.DashboardHandler, name='dashboard', strict_slash=True),
    RedirectRoute('/courses', handlers.CoursesHandler, name='courses', strict_slash=True),
    RedirectRoute('/course/practice', handlers.CoursePracticeHandler, name='course-practice', strict_slash=True),
    RedirectRoute('/course/practice/resume', handlers.CoursePracticeResumeHandler, name='course-practice-resume', strict_slash=True),
    RedirectRoute('/course/learn/resume', handlers.CourseLessonResumeHandler, name='course-lesson-resume', strict_slash=True),
    RedirectRoute('/course/practice/viewer', handlers.CoursePracticeViewerHandler, name="course-practice-viewer", strict_slash=True),
    #RedirectRoute('/course/learn/<course_id>', handlers.CourseLearnHandler, name='course-learn', strict_slash=True),
    RedirectRoute('/course/learn', handlers.CourseLearnHandler, name='course-learn', strict_slash=True),
    RedirectRoute('/visualization', handlers.VisualizationHandler, name='visualization', strict_slash=True),
    RedirectRoute('/teacher', handlers.TeacherHandler, name='teacher-page'
                                                            '', strict_slash=True),
    RedirectRoute('/', handlers.HomeRequestHandler, name='home', strict_slash=True),

]


def get_routes():
    return _routes


def add_routes(app):
    if app.debug:
        secure_scheme = 'http'
    for r in _routes:
        app.router.add(r)
