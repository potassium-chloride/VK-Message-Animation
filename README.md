# VK-Message-Animation
Make simple text animation in VK Messages by messages.edit

Создаёт простую текстовую анимацию в диалогах ВКонтакте путём редактирования сообщений.
Использование: укажите в коде Ваш ```access_token``` или сохраните его как текстовый файл ~/bin/.token с доступом к личным сообщениям (смотрите документацию ВКонтакте https://vk.com/dev/implicit_flow_user)
В качестве демонстрации можно вызвать скрипт, передав ему как аргумент командной строки peer_id диалога (см. https://vk.com/dev/messages.send).
После запуска в диалоге должен появиться ProgressBar, когда он дойдёт до конца, скрипт завершит работу.
Если скрипт отображает более 20 кадров, то VK просит капчу. Она отобразится на экране, после её разгадывания нужно будет запомнить код и ввести его в следующем окне. Учитывайте это.
