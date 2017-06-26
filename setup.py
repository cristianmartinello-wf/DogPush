from setuptools import find_packages, setup

from pip.req import parse_requirements


def get_version():
    import imp

    mod = imp.load_source('_meta', 'dogpush/_meta.py')

    return mod.version


def get_requirements(filename):
    try:
        from pip.download import PipSession

        session = PipSession()
    except ImportError:
        session = None

    reqs = parse_requirements(filename, session=session)

    return [str(r.req) for r in reqs]


def get_install_requires():
    return get_requirements('requirements.txt')


setup_args = dict(
    name='DogPush',
    version=get_version(),
    maintainer="InfRe Group",
    maintainer_email="infre@workiva.com",
    packages=find_packages(),
    install_requires=get_install_requires(),
    include_package_data=True,
    scripts=['scripts/dogpush']
)

if __name__ == '__main__':
    setup(**setup_args)
