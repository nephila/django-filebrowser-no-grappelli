from setuptools import setup, find_packages

setup(
    name='django-filebrowser',
    version='3.0',
    description='Media-Management with the Django Admin-Interface.',
    author='Patrick Kranzlmueller',
    author_email='patrick@vonautomatisch.at',
    url='http://code.google.com/p/django-filebrowser/',
    packages=find_packages(),
    package_data={
        'filebrowser': [
            'locale/*/LC_MESSAGES/*.po','locale/*/LC_MESSAGES/*.mo',
	    'media/filebrowser/css/*.css','media/filebrowser/js/*.js','media/filebrowser/img/*.gif','media/filebrowser/img/*.png',
	    'media/filebrowser/uploadify/*.*','media/filebrowser/uploadify/com/adobe/*/*.*','media/filebrowser/uploadify/com/adobe/*/*/*.*','media/filebrowser/uploadify/com/adobe/*/*/*/*.*',
	    'templates/filebrowser/*.html','templates/filebrowser/include/*.html'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
