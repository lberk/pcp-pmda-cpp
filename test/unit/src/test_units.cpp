//               Copyright Paul Colby 2013.
// Distributed under the Boost Software License, Version 1.0.
//       (See accompanying file LICENSE.md or copy at
//          http://www.boost.org/LICENSE_1_0.txt)

#include "pcp-cpp/units.hpp"

#include "gtest/gtest.h"

TEST(units, independent_values) {
    const pmUnits new_units = pcp::units(1,2,3, 4,5,6);
    EXPECT_EQ(1, new_units.dimSpace);
    EXPECT_EQ(2, new_units.dimTime);
    EXPECT_EQ(3, new_units.dimCount);
    EXPECT_EQ(4u, new_units.scaleSpace);
    EXPECT_EQ(5u, new_units.scaleTime);
    EXPECT_EQ(6, new_units.scaleCount);
}

TEST(units, lower_bound) {
    const pmUnits new_units = pcp::units(-8,-8,-8, 0,0,-8);
    EXPECT_EQ(-8, new_units.dimSpace);
    EXPECT_EQ(-8, new_units.dimTime);
    EXPECT_EQ(-8, new_units.dimCount);
    EXPECT_EQ(0u, new_units.scaleSpace);
    EXPECT_EQ(0u, new_units.scaleTime);
    EXPECT_EQ(-8, new_units.scaleCount);
}

TEST(units, upper_bound) {
    const pmUnits new_units = pcp::units(7,7,7, 15,15,7);
    EXPECT_EQ( 7, new_units.dimSpace);
    EXPECT_EQ( 7, new_units.dimTime);
    EXPECT_EQ( 7, new_units.dimCount);
    EXPECT_EQ(15u, new_units.scaleSpace);
    EXPECT_EQ(15u, new_units.scaleTime);
    EXPECT_EQ( 7, new_units.scaleCount);
}

TEST(units, underflow) {
    const pmUnits new_units = pcp::units(-9,-9,-9, -1,-1,-9);
    EXPECT_EQ( 7, new_units.dimSpace);
    EXPECT_EQ( 7, new_units.dimTime);
    EXPECT_EQ( 7, new_units.dimCount);
    EXPECT_EQ(15u, new_units.scaleSpace);
    EXPECT_EQ(15u, new_units.scaleTime);
    EXPECT_EQ( 7, new_units.scaleCount);
}

TEST(units, overflow) {
    const pmUnits new_units = pcp::units(8,8,8, 16,16,8);
    EXPECT_EQ(-8, new_units.dimSpace);
    EXPECT_EQ(-8, new_units.dimTime);
    EXPECT_EQ(-8, new_units.dimCount);
    EXPECT_EQ(0u, new_units.scaleSpace);
    EXPECT_EQ(0u, new_units.scaleTime);
    EXPECT_EQ(-8, new_units.scaleCount);
}
