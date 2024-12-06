add_executable(page_ordering main.cpp page_ordering.cpp)

add_executable(test_page_ordering test_page_ordering.cpp page_ordering.cpp)
target_link_libraries(test_page_ordering GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(test_page_ordering)