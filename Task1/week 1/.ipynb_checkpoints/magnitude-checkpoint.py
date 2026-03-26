{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "822d5722-2d5e-484d-8956-50a59b645c41",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sirius data\n",
    "apparentMagnitude = input(\"Input apparent magnitude:  \")\n",
    "absoluteMagnitude = input(\"Input absolute magnitude:  \")\n",
    "\n",
    "# The distance is related to the magnitudes as m-M=5.Log(d/10)\n",
    "# 1 Parsec = 3.26164 ly\n",
    "\n",
    "m = apparentMagnitude\n",
    "M = absoluteMagnitude\n",
    "\n",
    "d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
