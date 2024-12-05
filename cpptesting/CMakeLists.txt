add_executable(test_gtest test_gtest.cpp)
target_link_libraries(test_gtest GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(test_gtest)