### Nmf2Wav - Conversor de arquivos Nmf em Wav

#### Docker Run comand
 
```
 docker run --rm --name nmf2wav -it -p 5000:5000 matheus306/nmftowav
```

#### Exemplo Cliente Java


	/**
	 * Vai enviar o arquivo WAV para ser convertido pelo serviço em Python
	 * @param file - {@link File}
	 * @author Matheus Melo
	 */
	public void converter(File file) {
		if(!file.exists())
			logger.info("Não foi possível recuperar o arquivo para enviar ao conversor Python");

		HttpPost post = new HttpPost("http://localhost:5000/v1/nmftowav/upload");
		MultipartEntityBuilder builder = MultipartEntityBuilder.create();
		CloseableHttpClient client = HttpClients.createDefault();

		builder.addBinaryBody("files", file, ContentType.MULTIPART_FORM_DATA, file.getName());
		HttpEntity multipart = builder.build();

		post.setEntity(multipart);

		try {
			CloseableHttpResponse response = client.execute(post);
			HttpEntity entity = response.getEntity();
			if (entity != null) {
				Path destination = Paths.get("C:\\Temp\\2.0\\" + file.getName().replace("nmf", "wav"));

				if(destination.toFile().exists()) {
					destination.toFile().delete();
				}

				InputStream initialStream = entity.getContent();
				Files.copy(initialStream, destination);
				client.close();
				logger.info(String.format("Arquivo %s convertido com sucesso",  file.getName()));
			}

		} catch (ClientProtocolException e) {
			logger.info("Erro ao enviar o arquivo para o serviço Python", e.getMessage());
		} catch (IOException e) {
			logger.info("Erro ao enviar o arquivo para o serviço Python", e.getMessage());
		}
	}