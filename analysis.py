{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ba575944-e223-487b-9214-48d9f346e7e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Future value: 19671.51\n"
     ]
    }
   ],
   "source": [
    "capital = 10000\n",
    "rate = 0.07\n",
    "years = 10\n",
    "\n",
    "future_value = capital * (1 + rate) ** years\n",
    "\n",
    "print(\"Future value:\", round(future_value, 2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b558b80d-01c0-4912-b0cb-70c6ee4d2885",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Future value: 19671.51\n"
     ]
    }
   ],
   "source": [
    "capital = 10000\n",
    "rate = 0.07\n",
    "years = 10\n",
    "\n",
    "future_value = capital * (1 + rate) ** years\n",
    "\n",
    "print(\"Future value:\", round(future_value, 2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c2f44e3e-31de-4161-8281-51e9799f3229",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2273889015.py, line 16)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[6]\u001b[39m\u001b[32m, line 16\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mportfolio[\"Return_%\"] = (portfolio[\"Profit\"] / portfolio[\"Invested\"]) *\u001b[39m\n                                                                           ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# создаём портфель\n",
    "data = {\n",
    "    \"Asset\": [\"UK Bonds\", \"US ETF\", \"Crypto\", \"Cash GBP\"],\n",
    "    \"Invested\": [5000, 3000, 1000, 1000],\n",
    "    \"Current_Value\": [5400, 3300, 900, 1000]\n",
    "}\n",
    "\n",
    "portfolio = pd.DataFrame(data)\n",
    "\n",
    "# считаем прибыль\n",
    "portfolio[\"Profit\"] = portfolio[\"Current_Value\"] - portfolio[\"Invested\"]\n",
    "\n",
    "# считаем доходность в %\n",
    "portfolio[\"Return_%\"] = (portfolio[\"Profit\"] / portfolio[\"Invested\"]) *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6d8547e4-e86d-4a5c-bac7-769da19a588e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'portfolio' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m total_invested = \u001b[43mportfolio\u001b[49m[\u001b[33m\"\u001b[39m\u001b[33mInvested\u001b[39m\u001b[33m\"\u001b[39m].sum()\n\u001b[32m      2\u001b[39m total_current = portfolio[\u001b[33m\"\u001b[39m\u001b[33mCurrent_Value\u001b[39m\u001b[33m\"\u001b[39m].sum()\n\u001b[32m      4\u001b[39m total_return = (total_current - total_invested) / total_invested * \u001b[32m100\u001b[39m\n",
      "\u001b[31mNameError\u001b[39m: name 'portfolio' is not defined"
     ]
    }
   ],
   "source": [
    "total_invested = portfolio[\"Invested\"].sum()\n",
    "total_current = portfolio[\"Current_Value\"].sum()\n",
    "\n",
    "total_return = (total_current - total_invested) / total_invested * 100\n",
    "\n",
    "print(\"Total portfolio return:\", round(total_return, 2), \"%\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "799392ff-9215-42d0-9b73-f69bbabf9d72",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.14.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
