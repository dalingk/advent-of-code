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

TEST(day5, correct_update)
{
    PageOrderings example_orderings = {
        { 97, { 13, 47, 29, 75 } }, { 75, { 29, 47, 13 } }, { 29, { 13 } }, { 47, { 13, 29 } }
    };
    PageUpdate to_correct = { 97, 13, 75, 29, 47 };
    PageUpdate is_correct = { 97, 75, 47, 29, 13 };

    EXPECT_EQ(correct_update(to_correct, example_orderings), is_correct);
}

TEST(day5, correct_update_complex)
{
    PageOrderings example_orderings = { { 6, { 7 } }, { 7, { 8 } }, { 8, { 9 } }, { 9, { 10 } } };
    PageUpdate to_correct = { 10, 9, 8, 7, 6 };
    PageUpdate is_correct = { 6, 7, 8, 9, 10 };

    EXPECT_EQ(correct_update(to_correct, example_orderings), is_correct);
}