# Django

## 들어가기

주로 docs.djangoproject의 tutorial을 따라하며,  모르는 부분은 다른 사이트들을 참고 할 것이다. 

참고 사이트: [Django 훑어보기](https://docs.djangoproject.com/ko/2.0/intro/overview/)

Django와 데이터 드리븐 웹 어플리케이션의 작성방법을 배울 수 있다.

 **Django : 보편적인 웹 개발 업무를 빠르고 쉽게 만들어주도록 설계되었다. 

**데이터 드리븐 방식: 코드에서 변동이 가능한 데이터(숫자/문자 등)들을 개발자가 하드코딩 하지 않고 외부 파일이나 웹에서 불러 들여와 참조하여 코딩하는 방식을 말한다. 기획자와 분업을해야 할 때 특히 기획자가 숫자값을 바꿔가며 여러번 테스트 해야 할 때 유용하다. 

즉, 값을 바꿀 때마다 개발자에게 "빌드해 주세요!"라는 불상사를 막을 수 있다. 

<details>

<summary> 데이터 드리븐과 참고 사이트 정리</summary>

[gpgstudy_데이터 드리븐과 코드](http://www.gpgstudy.com/forum/viewtopic.php?t=4163)

[gpgstudy_자연스러운 하드코딩](http://www.gpgstudy.com/forum/viewtopic.php?t=4395&start=0&postdays=0&postorder=asc&highlight=%C7%CF%B5%E5+%BD%BA%C5%B3)



**데이터 드리븐 설계의 고전적 의미**

코드에 값을 집어넣지 않고, <span style="color=tomato"> 코드와 데이터를 분리하고 데이터를 바꿔줌으로서</span> 수많은 다양성을 만드는 것이다. 

**하드코딩의 문제**

코딩 자체가 하나의 특정 데이터를 지칭하고 있다면, 
(방대한 데이터가 있을경우) 방대한 데이터 하나하나 마다 코드 한벌씩 존재해야 돌아간다. 

그렇다면, 어떤 특정한 기획사항이 특정 코딩을 요구할때의 처리사항을 어떻게 처리하면 좋을까를 고민해야 한다.

데이터 드리븐의 주요한 목적과 장점은, 데이터로서 어떤 무언가와 다양성을 성취하는 것이다. 

</details>

**Django**

Django framework의 동작원리
참고사이트: [django 1년차 개발자가 쓰는 퍼펙트 django 강의](https://blog.naver.com/93immm/221121976376)

urls > views > html

```
1. url을 먼저 받는다.
2. url에 해당하는 함수로 이동시킨다. 
3. back-end 작업
4. html을 렌더링해서 띄워준다.
```

## Django로 앱 작성하기

### #1.프로젝트 생성

* cmd창에서 프로젝트 생성

```
[path]> django-admmin startproject [포로젝트명]
# >django-admin startproject django2
```

* 서버실행 해보기

```
python manage.py runserver
```

Starting development server at http://127.0.0.1:8000/

### #2. 화면 띄우기

간단하게 화면에 정보를 띄울 수 있도록 한다.

* news/views.py

첫번째 view 페이지를 만들고 view를 확인, index 페이지를 만들어 잘 실행되는지 확인하고자 한다.

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

* news/urls.py

URL 패턴 설정(라우팅 설정)

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

<details>

<summery>URL 설정 자세히</summery>

참고 페이지: [첫 번째 장고 앱 작성하기, part1](https://docs.djangoproject.com/ko/2.0/intro/tutorial01/)

#### 1. URLconf 생성

<span style="color:grey">view를 호출하려면 이와 연결된 URL이 있어야 한다. 이를 위해 URLconf가 사용된다.</span>

* `news 디렉토리`에 `urls.py`를 생성

URLconf를 생성하기 위함이다

#### 2. app의 URL 패턴 설정

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

path('', views.index, name='index')

기본 루트 '', index 페이지를 찾아가며, 그 view페이지의 이름은 index이다. 

#### 3. 프로젝트 단의 url설정 

최상위 U해야한다. RLconf에서 news.urls 모듈을 바로보게 설정해야한다. 

* django2/urls.py

```python
# django.urls.include을 import
# from django.urls import include

from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
]
```

>* news/urls.py
>  path('', views.index, name='index'),
>* django/urls.py
>  path('news/', include('news.urls')),

include()함수는 다른 URLconf들을 참조할 수 있도록 도와준다. 

</details>





```
python manage.py runserver
```

http://localhost:8000/news/



### #3.모델 설계

`data-model syntax'는 모델을 풍부하게 표현할 수 있도록 한다. 기존의 데이터베이스 스키마 문제들을 해결할 수 있다. 

* django2/news/models.py

  ```python
  from django.db import models

  class Reporter(models.Model):
      full_name = models.CharField(max_length=70)

      def __str__(self):
          return self.full_name

  class Article(models.Model):
      pub_date = models.DateField()
      headline = models.CharField(max_length=200)
      content = models.TextField()
      reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

      def __str__(self):
          return self.headline
  ```

  ​

<details>

<summery>모델 설계 자세히</summery>

#### 1. app을 생성한다 

```
> python manage.py startapp news
```

news라는 디렉토리가 생성된 것을 볼 수 있다. 
`news` 디렉토리 구조는 new 어플리케이션의 집이 되어준다. 

#### 2. 데이터베이스 설치 

참고 페이지: [첫 번째 장고 앱 작성하기, part2](https://docs.djangoproject.com/ko/2.0/intro/tutorial02/)

* django2/settings.py 에서 database를 설정
  <span style="color:grey">Django 설정을 모듈 변수로 표현한 보통의 Python 모듈이다. 기본적으로는 SQLite를 사용하도록 구성되어 있으며, 여기서는 SQLite를 사용한다.</span>

* 데이터베이스 테이블을 생성

  terminal에 명령어를 실행

```python
> python manage.py migrate
```

<span style="color:grey">migrate 명령은 INSTALLED_APPS의 설정을 탐색, django3/setting.py의 데이터베이스 설정과 app과 함께 제공되는 데이터베이스 migrations에 따라, 필요한 데이터베이스 테이블을 생성한다.</span>

#### 3. 모델 만들기

모델은 데이터에 관한 단 하나의 **진리의원천**이다. 저장하는 데이터의 <span style="color:red">필수적인 필드</span>와 <span style="color:red">동작</span>들을 포함하고 있다. 

**모델 : 부가적인 메타데이터를 가진 데이터베이스의 구조를 말한다.

* news/models.py

  Reporter모델과 Article 모델 

  ```python
  from django.db import models

  # Create your models here.
  class Reporter(models.Model):
      full_name = models.CharField(max_length=70)

      def __str__(self):
          return self.full_name

  class Article(models.Model):
      pub_date = models.DateField()
      headline = models.CharField(max_length=200)
      content = models.TextField()
      reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
  ```

#### 4. 모델의 활성화

모델에 대한 코드가 Django에게는 상당한 양의 정보를 전달한다. 이 정보가 하는 역할을 정의하자면 <u>아래</u>와 같다.

> * 이 app (여기서는 news app)에 대하여 데이터베이스 스키마 생성
> * Reporter와 Article 객체에 접근하기 위한 Python 데이터베이스 접근 API를 생성

* django3/setting.py

app을 현재의 project에 **포함**시켜야 한다.

<p style="color:grey">가장 먼저 현재 project에게 news app이 설치되어 있다는 것을 알려야 한다.</p>

```python
# 'news.apps.NewsConfig'를 추가

INSTALLED_APPS = [
    'news.apps.NewsConfig',
    # ... 
    # ... ,
]
```

 `news.apps.NewsConfig`은 `news/apps.py` 파일에 정의되어 있다.

* 모델을 변경시킨 사실을 알린다.

**migration: Django가 모델의 변경사항을 저장하는 방법으로써, 디스크상의 파일로 존재한다. (news/migrations/0001_initial.py) 파일로 저장된 새 모델에 대한 migration을 읽어볼 수 있다. 

terminal

```
python manage.py makemigrations news
```

> Migrations for 'news':
>   news\migrations\0001_initial.py
>
>     - Create model Article
>     - Create model Reporter
>     - Add field reporter to article

news 디렉토리에 `db.sqlite3`가 생긴 것을 볼 수 있다. 

* 모델에서의 변경사항들과 데이터베이스의 스키마의 동기화

<span style="color:grey">[`migrate`](https://docs.djangoproject.com/ko/2.0/ref/django-admin/#django-admin-migrate) 명령은 아직 적용되지 않은 모든 migration 들을 수집하여 이를 실행합니다.</span>

terminal

```
> python manage.py migrate
```

</details>

### #3.URL 설계

`#2 화면띄우기`에서 이미했던 URL설계를 심화해서 다룬다. 복습을 해보면, URL을 설계하기 위해서 URLconf 파이썬 모듈을 생성해야 한다. 

**URLconf: URL패턴과 파이썬 콜백 함수 간의 간단한 매핑 정보를 담고 있는 만들고자 하는 앱에 대한 목차이다. 

*  django2/news/urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]
```

1. 위 코드는 URL 경로들을 파이썬 콜백 함수들("views")로 연결해 준다.
2. 경로를 나타내는 문자열들은 매개 변수 태그들을 사용하여 URL로 부터 값을 받아온다.
3. 사용자에게 page를 요청 받았을 경우, Django는 각 경로를 순서대로 실행하고, 요청된URL과 일치하는 첫번째 것에서 정지한다. 
4. URL패턴들 중 하나가 매치하면, Django는 주어진 파이썬 함수인 view를 호출한다.
   <span style="color:grey">각각의 view에는 요청 메타데이터가 포함된 요청 개체와 패턴에 잡힌 값이 전달 된다. </span> 




