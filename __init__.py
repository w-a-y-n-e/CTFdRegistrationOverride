import os
from CTFd.utils.plugins import override_template

def load(app):
    print("Loading.........................")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(dir_path, 'confirm_override.html')
    override_template('confirm.html', open(template_path).read())
    template_path = os.path.join(dir_path, 'register_override.html')
    override_template('register.html', open(template_path).read())