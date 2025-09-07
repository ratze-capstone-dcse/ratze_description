cmake_minimum_required(VERSION 3.8)
project(ratze_description)

find_package(ament_cmake REQUIRED)

foreach(dir . )
	install(DIRECTORY ${dir}
		DESTINATION share/${PROJECT_NAME})
endforeach(dir)

ament_package()