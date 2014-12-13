# Compiler
set (CMAKE_C_COMPILER "cc" CACHE STRING "")
set (CMAKE_CXX_COMPILER "CC" CACHE STRING "")

# Disable testing for PISM's prerequisites
set (Pism_LOOK_FOR_LIBRARIES OFF CACHE BOOL "")

# Installation path
set (CMAKE_INSTALL_PREFIX "$ENV{HOME}/pism/" CACHE STRING "")

# General compilation/linking settings
set (Pism_ADD_FPIC OFF CACHE BOOL "")
set (Pism_LINK_STATICALLY ON CACHE BOOL "")

# No Proj.4 on fish.arsc.edu
set (Pism_USE_PROJ4 OFF CACHE BOOL "")
# No TAO on fish.arsc.edu
set (Pism_USE_TAO OFF CACHE BOOL "")
# No PNetCDF on fish (alas)
set (Pism_USE_PNETCDF OFF CACHE BOOL "")

# Set the custom GSL location
set (GSL_LIBRARIES "$ENV{GSL_ROOT}/lib/libgsl.a;$ENV{GSL_ROOT}/lib/libgslcblas.a" CACHE STRING "" FORCE)
set (GSL_INCLUDES  "$ENV{GSL_ROOT}/include" CACHE STRING "" FORCE)

# Set custom UDUNITS2 location
set (UDUNITS2_ROOT "/usr/local/pkg/udunits/udunits-2.1.24.gnu")
set (UDUNITS2_LIBRARIES "${UDUNITS2_ROOT}/lib/libudunits2.a;/usr/lib64/libexpat.a" CACHE STRING "" FORCE)
set (UDUNITS2_INCLUDES  "${UDUNITS2_ROOT}/include" CACHE STRING "" FORCE)
