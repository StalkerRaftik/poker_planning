# Codraw - anime website
<details>
<summary>Site images</summary>
  
![image](https://user-images.githubusercontent.com/24423216/159034694-3a12f103-90d8-496c-bcfc-39af1421b11e.png)
![image](https://user-images.githubusercontent.com/24423216/159121701-5f0f6c69-3840-44ac-ad63-db9071a0a8b5.png)
![image](https://user-images.githubusercontent.com/24423216/159035798-6f2e7bf8-48ff-4409-8b87-697058c82358.png)
![image](https://user-images.githubusercontent.com/24423216/159035906-3d8b5796-1b9d-4d67-93a8-5794b51977a9.png)
  
</details>

## Requirements:
1. Docker/docker-compose/buildkit:  [linux](https://docs.docker.com/engine/install/ubuntu/) or [windows](https://www.docker.com/products/docker-desktop/)

## Start dev server: 
1. Go to `dev` folder;
2. Up containers with build flag:
   1. Linux: `COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up --build`
   2. Windows: `docker-compose up --build`
3. It's done!

- Site: http://localhost:8080
- Admin-panel: http://localhost:8000/admin/
- OpenAPI: http://localhost:8000/api/endpoint/

## Deploy server:
Deployment not implemented for now

## Celery tasks:
2. Start redis via `docker-compose up redis`
3. Start beat via `celery -A codraw beat` (only in project container)
4. Create workers via `celery -A codraw worker --loglevel=debug --concurrency=*YOUR WORKERS COUNT*`(only in project container)


## Useful Commands:
- Run tests: `tox` (0 tests so far 0_0, technical debt created ✓)
- Load anime data from csv file(run from `dev` or `prod` folder context only): `docker-compose exec backend python manage.py loadcsv path/to/dataset.csv *threads number*`

Supported dataset: [Dataset](https://www.kaggle.com/marlesson/myanimelist-dataset-animes-profiles-reviews/code).
