#include "page_ordering.h"
#include <gtest/gtest.h>

std::istringstream valid_inputs("1|2\n2|10\n10|100\n\n1,2,10,100\n");
PageOrderings orderings = { { 1, { 2 } }, { 2, { 10 } }, { 10, { 100 } } };

TEST(day5, load_file)
{
    PageUpdates expected_updates = { { 1, 2, 10, 100 } };

    auto [orders, updates] = load_file(valid_inputs);

    EXPECT_EQ(orders, orderings);
    EXPECT_EQ(updates, expected_updates);
}

TEST(day5, valid_page_update)
{
    PageUpdate valid_update = { 1, 2, 10, 100 };

    EXPECT_TRUE(is_valid_page_update(valid_update, orderings));
}

TEST(day5, invalid_page_update)
{
    PageUpdate invalid_update = { 100, 1, 2, 10 };
    EXPECT_FALSE(is_valid_page_update(invalid_update, orderings));
}