from app import create_app,db
import click
import os 
import sys

COV=None
if os.getenv("FLASK_COVERAGE"):
    import coverage
    COV = coverage.coverage(branch=True,include="app/*")
    COV.start()


app = create_app('default')

from app.index.models import *
@app.shell_context_processor
def shell_context_processor():
    return {"db":db}

@app.cli.command()
def deploy():
    print("Hello")

@app.cli.command()
@click.option('--coverage/--no-coverage', default=False,
              help='Run tests under code coverage.')
def test(coverage):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'
        sys.exit(subprocess.call(sys.argv))

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
