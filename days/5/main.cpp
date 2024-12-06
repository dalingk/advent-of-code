#include "page_ordering.h"
#include <fstream>
#include <iostream>

int
main()
{
    std::string input_filename("./days/5/resources/input.txt");
    std::ifstream input_file(input_filename);
    if (!input_file.is_open()) {
        std::cerr << "Failed to open" << input_filename << std::endl;
    }

    try {
        auto [orders, updates] = load_file(input_file);
        PageUpdates incorrect_updates = {};
        int middle_sum = 0;
        int corrected_sum = 0;
        for (auto& update : updates) {
            if (is_valid_page_update(update, orders)) {
                middle_sum += update[update.size() / 2];
            } else {
                incorrect_updates.push_back(update);
            }
        }
        std::cout << "Sum of middle updates: " << middle_sum << std::endl;
        for (auto& update : incorrect_updates) {
            auto corrected_update = correct_update(update, orders);
            corrected_sum += corrected_update[update.size() / 2];
        }
        std::cout << "Sum of median for corrected updates: " << corrected_sum << std::endl;
    } catch (std::string error) {
        std::cerr << error << std::endl;
        return 1;
    }

    return 0;
}