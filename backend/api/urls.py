from django.urls import path

from . import views

urlpatterns = [
    path('auth/token/login/',
         views.LoginAPIView.as_view(), name='login'),
    path('auth/token/logout/',
         views.LogoutAPIView.as_view(), name='logout'),
    path('users/', views.UsersDispatcherAPIView.as_view(),
         name='users_dispatcher'),
    path('users/set_password/',
         views.ChangePasswordAPIView.as_view(), name='change_password'),
    path('users/subscriptions/',
         views.SubscriptionsListAPIView.as_view(), name='subscriptions_list'),
    path('users/<int:pk>/subscribe/',
         views.SubscriptionsAPIView.as_view(), name='subscription_add'),
    path('users/<str:pk>/',
         views.UserProfileAPIView.as_view(), name='user_profile'),
    path('tags/', views.TagsListAPI.as_view(), name='tags_list'),
    path('tags/<int:pk>/', views.TagAPIView.as_view(), name='tag_by_id'),
    path('ingredients/',
         views.IngredientsListAPI.as_view(), name='ingredients_list'),
    path('ingredients/<int:pk>/',
         views.IngredientAPIView.as_view(), name='ingredient_by_id'),
    path('recipes/',
         views.RecipeDispatcherAPIView.as_view(), name='recipe_list'),
    path('recipes/download_shopping_cart/',
         views.DownloadShoppingCartAPIView.as_view(),
         name='download_shopping_cart'),
    path('recipes/<int:pk>/',
         views.RecipeByIDDispatcherAPIView.as_view(), name='recipe_by_id'),
    path('recipes/<int:pk>/shopping_cart/',
         views.ShoppingCartAPIView.as_view(),
         name='add_to_shopping_cart'),
    path('recipes/<int:pk>/favorite/',
         views.FavoriteAPIView.as_view(),
         name='add_to_favorite'),

]
