#include <gtest/gtest.h>

// Basic file to ensure CMake and Google Test are working

TEST(HelloTest, BasicAssertions) {
    EXPECT_STRNE("Hello", "world");
}