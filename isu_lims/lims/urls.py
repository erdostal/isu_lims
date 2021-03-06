from django.urls import path
from . import views
from .views import GenusDetailView
from .views import SubgenusDetailView
from .views import GenomeDetailView
from .views import SpeciesDetailView
from .views import AccessionDetailView
from .views import PlantDetailView
from .views import SeedPacketDetailView
from .views import SeedDetailView
from .views import ProjectDetailView
from .views import SampleDetailView
from .views import newseedpacket

urlpatterns = [
    path('', views.index, name='index'),
    path('genera', views.genera, name='genera'),
    path('subgenera', views.subgenera, name='subgenera'),
    path('genome', views.genome, name='genome'),
    path('species', views.species, name='species'),
    path('accession', views.accession, name='accession'),
    path('plant', views.plant, name='plant'),
    path('seedpacket', views.seedpacket, name='seedpacket'),
    path('seed', views.seed, name='seed'),
    path('project', views.project, name='project'),
    path('sample', views.sample, name='sample'),
    path('genus/<int:pk>/', GenusDetailView.as_view(), name='genus-detail'),
    path('seedpacket/new', views.newseedpacket, name='newseedpacket'),
    path('genus/new', views.newgenus, name='newgenus'),
    path('subgenus/new', views.newsubgenus, name='newsubgenus'),
    path('genome/new', views.newgenome, name='newgenome'),
    path('species/new', views.newspecies, name='newspecies'),
    path('accession/new', views.newaccession, name='newaccession'),
    path('plant/new', views.newplant, name='newplant'),
    path('seed/new', views.newseed, name='newseed'),
    path('project/new', views.newproject, name='newproject'),
    path('sample/new', views.newsample, name='newsample'),
    path('subgenus/<int:pk>/', SubgenusDetailView.as_view(), name='subgenus-detail'),
    path('genome/<int:pk>/', GenomeDetailView.as_view(), name='genome-detail'),
    path('species/<int:pk>/', SpeciesDetailView.as_view(), name='species-detail'),
    path('accession/<int:pk>/', AccessionDetailView.as_view(), name='accession-detail'),
    path('plant/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
    path('seedpacket/<int:pk>/', SeedPacketDetailView.as_view(), name='seedpacket-detail'),
    path('seed/<int:pk>/', SeedDetailView.as_view(), name='seed-detail'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('sample/<int:pk>/', SampleDetailView.as_view(), name='sample-detail'),

]
